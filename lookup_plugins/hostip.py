#!/usr/bin/python

# Written By - Rishabh Das <rishabh5290@gmail.com>
#
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option) any
# later version. See http://www.gnu.org/copyleft/gpl.html for the full text of
# the license.

##############################################################################

import socket


class LookupModule(object):

    '''
    Returns IP of host
    '''

    def __init__(self, basedir=None, **kwargs):
        self._basedir = basedir

    def run(self, hostname, **kwargs):
        try:
            host_detail = socket.gethostbyname(hostname)
        except:
            host_detail = 'Invalid Hostname'
        return host_detail
