# -*- coding: utf-8 -*-

"""
:Copyright: 2007-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from __future__ import unicode_literals
from unittest import TestCase

from nose2.tools import params

from syslog2irc import irc_channel_joined, Processor, shutdown_requested


class ProcessorTestCase(TestCase):

    def test_shutdown_flag_set_on_shutdown_signal(self):
        processor = self._create_processor()
        self.assertEqual(processor.shutdown, False)

        shutdown_requested.send()
        self.assertEqual(processor.shutdown, True)

    def test_ports_to_channel_names_mapping_extended_on_join_signal(self):
        channel_names_to_ports = {
            '#example1': {514},
            '#example2': {514, 55514},
        }

        processor = self._create_processor(
            channel_names_to_ports=channel_names_to_ports)
        self.assertEqual(processor.ports_to_channel_names, {})

        irc_channel_joined.send(channel='#example1')
        self.assertEqual(processor.ports_to_channel_names, {
            514: {'#example1'},
        })

        irc_channel_joined.send(channel='#example2')
        self.assertEqual(processor.ports_to_channel_names, {
            514: {'#example1', '#example2'},
            55514: {'#example2'},
        })

    def _create_processor(self, announcer=None, channel_names_to_ports=None):
        processor = Processor(announcer, channel_names_to_ports or {})
        processor.connect_to_signals()
        return processor