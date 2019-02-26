#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  History command
# ===============================

from core.commands.Command import Command
from core.Saver import Saver

class DoHistory(Command):
    ID = 'history'
    HELP = 'Outputs all the data from the local storage'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        print("Executing History Command")
        saver = Saver()
        history = saver.getHistory()
        specified_services = [serv.ID for serv in self._services]

        if self._args.only != None:
            arg_services = self._args.only[0].split(',')
            # check if every specified service is in the available services list
            for s in arg_services:
                if s not in [serv.ID for serv in self._services]:
                    print("Invalid service: %s\nExiting" % s)
                    exit(-1)

            # remaining services are the ones in the 'only' argument list
            specified_services = [serv.ID for serv in self._services if serv.ID in arg_services]

        # print out the history
        for sid in history.keys():
            if sid in specified_services:
                print("=========[ %s ]=========" % (sid))
                ordered_dates = saver.order_entries_dic(history[sid])
                for date, status in history[sid].items():
                    print("  -> %s %s" % (date, status))
                print("==============================")
            