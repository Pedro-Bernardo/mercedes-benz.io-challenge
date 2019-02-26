#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Services command
# ===============================

from core.commands.Command import Command

class DoServices(Command):
    ID = 'services'
    HELP = 'Lists all known services'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        for service in self._services:
            print("[ %s ] -> id: %s - url: %s" % (service.getName(), service.ID, service.getURL()))
