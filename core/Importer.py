import json
import csv
import datetime
from core.Saver import Saver

class Importer:
    def __init__(self, services):
        self.local_storage = '../history.json'
        self.saver = Saver()
        self.allowed_extensions = ['txt', 'json']
        self.services = services

    def json(self, data, path=None):
        pass

    def csv(self, path=None):
        pass

    def is_valid_extension(self, path):
        ext = path.split('.')[-1]
        
        return ext in self.allowed_extensions

    def import_file(self, path, merge=False):
        # check extension
        if not self.is_valid_extension(path):
            print("Invalid file format. Exiting...")
            exit(-1)
        print(path)
        external_data = self.load(path)
        print("EXTERNAL", external_data)
        self.check_integrity(external_data)

        # if it passed the integrity check, we can save it as our local history file
        if not merge:   
            self.saver.overwrite_history(external_data)

        else:
            sids = [s.ID for s in self.services]
            history = self.saver.getHistory()   
            print("HISTORY", history)
            final = {}
            print(sids)
            try:
                for sid in sids:
                    # join the dictionaries
                    final[sid] = {**history[sid], **external_data[sid]}
            except KeyError as err:
                if sid in history.keys():
                    # then external_data caused the exception
                    external_data[sid] = {}
                else:
                    # then history caused the exception
                    history[sid] = {}

                final[sid] = {**history[sid], **external_data[sid]}
            
            print("FINAL", final)
            self.saver.overwrite_history(final)

    def check_integrity(self, data):
        sids = [s.ID for s in self.services]

        # validate services
        for sid in data.keys():
            if sid not in sids:
                print("Invalid service. Exiting...")
                exit(-1)

        # validate dates
        try:
            for sid, entries in data.items():
                for date, value in entries.items():
                    datetime.datetime.strptime(date, "%x %X")
        except ValueError:
            print("Invalid date format. Exiting...")
            exit(-1)

    def load(self, path):
        # try to open the file
        try:
            file = open(path, "r")
        except OSError as err:
            # if it doesn't exist or permission is denied
            print("OS error: {0}".format(err))
            exit(-1)
            
        # try except in case there isn't any data in the file
        try:
            storage = json.load(file)
            file.close()
        except json.decoder.JSONDecodeError as err:
            storage = {}
        
        return storage

        