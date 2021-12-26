#!/usr/bin/python

# Written By - Rishabh Das <rishabh5290@gmail.com>
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option) any
# later version. See http://www.gnu.org/copyleft/gpl.html for the full text of
# the license.

##############################################################################

import socket

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    '''
    Returns IP of host
    '''

    def __init__(self, basedir=None, **kwargs):
        self._basedir = basedir

    def run(self, hostname, inject=None, **kwargs):
        host_detail = []
        for h in hostname:
            try:
                host_detail.append(socket.gethostbyname(h))
            except:
                host_detail.append('Invalid Hostname')
        return host_detail
