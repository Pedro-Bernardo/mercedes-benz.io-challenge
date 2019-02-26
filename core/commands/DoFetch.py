#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Fetch command
# ===============================
  
  
from core.commands.Command import Command
from core.commands.DoPoll import DoPoll
from core.PeriodicTimer import PeriodicTimer
import sched, time

class DoFetch(Command):
    ID = 'fetch'
    HELP = 'Retrieves the status from of all configured services'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
        self._refresh = 5
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        # the Poll command handles the only and exclude options
        poll_command = DoPoll(self._services, self._args)

        if self._args.refresh:
            self._refresh = self._args.refresh

        # execute the poll and sleep for the specified refresh rate
        try:
            while True:
                poll_command.execute()
                time.sleep(self._refresh)
        except KeyboardInterrupt:
            print('Program was interrupted. Exiting...')

