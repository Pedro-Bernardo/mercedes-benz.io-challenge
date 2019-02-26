#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Restore command
# ===============================

from core.commands.Command import Command
from core.Importer import Importer

class DoRestore(Command):
    ID = 'restore'
    HELP = 'Imports the internal state from another run or app'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        importer = Importer(self._services)
        
        importer.import_file(self._args.path, self._args.merge)
