#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
syslog2IRC
==========

Receive syslog messages via UDP and show them on IRC.

:Copyright: 2007-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:Date: 09-Sep-2015
:License: MIT, see LICENSE for details.
:Version: 0.9.2-dev
"""

from syslog2irc.argparser import parse_args
from syslog2irc.irc import Channel
from syslog2irc.main import start
import json


def start_with_args(routes, **options):
    """Start the IRC bot and the syslog listen server.

    All arguments (except for routes) are read from the command line.
    """
    args = parse_args()

    start(args.irc_server, args.irc_nickname, args.irc_realname, routes,
          ssl=args.irc_server_ssl, **options)


if __name__ == '__main__':
    # load config from file
    config = json.load(open("sample_config.json"))
    # Create an dictionary of Channel objects
    channel_list = {}
    for k,v in config['channels'].items():
        channel_list[k] = Channel(k,**v)

    # Create route mappings
    routes = {}
    for i in config['routes']:
        routes[i['port']] = []
        for j in i['channel']:
            routes[i['port']].append(channel_list[j])

    start_with_args(routes)
