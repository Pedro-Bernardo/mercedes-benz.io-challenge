#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Poll command
# ===============================

from core.commands.Command import Command
from core.StatusChecker import StatusChecker
from core.Saver import Saver
import json


class DoPoll(Command):
    ID = 'poll'
    HELP = 'Retrieves the status from of all configured services'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
        self._saver = Saver()
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        st = StatusChecker()
        status_list = []

        if self._args.only != None:
            arg_services = self._args.only[0].split(',')
            # check if every specified service is in the available services list
            for s in arg_services:
                if s not in [serv.ID for serv in self._services]:
                    print("Invalid service: %s\nExiting" % s)
                    exit(-1)

            remaining_services = [serv for serv in self._services if serv.ID in arg_services]

        elif self._args.exclude != None:
            arg_services = self._args.exclude[0].split(',')
            # check if every specified service is in the available services list
            for s in arg_services:
                if s not in [serv.ID for serv in self._services]:
                    print("Invalid service: %s\nExiting" % s)
                    exit(-1)

            remaining_services = [serv for serv in self._services if serv.ID not in arg_services]
        else:
            remaining_services = self._services

        for service in remaining_services:
            status_list.append(service.accept(st))


        self._saver.json(status_list)

        for s in status_list:
            print(s)
