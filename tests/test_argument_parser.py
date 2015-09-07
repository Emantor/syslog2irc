# -*- coding: utf-8 -*-

"""
:Copyright: 2007-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from __future__ import unicode_literals
from unittest import TestCase

from nose2.tools import params

from syslog2irc import parse_irc_server_arg


class ArgumentParserTestCase(TestCase):

    @params(
        ('localhost',      'localhost', 6667),
        ('127.0.0.1',      '127.0.0.1', 6667),
        ('127.0.0.1:6669', '127.0.0.1', 6669),
    )
    def test_parse_irc_server_arg(self, arg_value, expected_host, expected_port):
        actual = parse_irc_server_arg(arg_value)

        self.assertEqual(actual.host, expected_host)
        self.assertEqual(actual.port, expected_port)
