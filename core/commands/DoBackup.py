#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Backup command
# ===============================


from core.commands.Command import Command
from core.Saver import Saver

class DoBackup(Command):
    ID = 'backup'
    HELP = 'Backs up the current internal state to a file'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        saver = Saver()
        if self._args.format != None:
            saver.backup(self._args.path, self._args.format)
        else:
            saver.backup(self._args.path)
            
        print("Backup to %s was succesfull." % self._args.path)
                