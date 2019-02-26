import json
import csv
import datetime

class Saver:
    def __init__(self):
        self.local_storage = '../history.json'

    def json(self, data, path=None):
        #example
        #[gitlab] 02/24/19 17:36:20 - up
        if path:
            storage_location = path
        else:
            storage_location = self.local_storage

        try:
            file = open(storage_location, "r")

        except OSError as err:
            try:
                file = open(storage_location, "w+")
            except OSError as err:
                print("OS error: {0}".format(err))
                exit(-1)
            
        try:
            storage = json.load(file)
            file.close()
        except json.decoder.JSONDecodeError as err:
            storage = {}
        
        # if the keys are not all saved, join the dictionaries to avoid data loss
        # due to the json's dump behavior

        stored_ids = storage.keys()

       
            # assume there is already data in the history file
        for line in data:
            try:
                tokens = line.split(' ')
                service_id = tokens[0][1:-1]
                date = tokens[1] + ' ' + tokens[2]
                status = ''.join(tokens[4:])

                storage[service_id][date] = status

            except KeyError:
                # if there is a service id that hasn't been stored yet
                # initialize it's dictionary entry and then write to it
                tokens = line.split(' ')
                service_id = tokens[0][1:-1]
                date = tokens[1] + ' ' + tokens[2]
                status = ''.join(tokens[4:])

                storage[service_id] = {}
                storage[service_id][date] = status

        # finally, dump the json to the file
        with open(storage_location, 'w') as file:
            json.dump(storage, file)

    def csv(self, path=None):
        #example
        if path:
            if path.split('.')[-1] != 'csv':
                print("Invalid format. Exiting...")
                exit(-1)
            
            storage_location = path
        else:
            storage_location = self.local_storage

        
        # now the correct path is in storage_location
        try:
            # try to open it
            storage = open(storage_location, 'w')
        except OSError as err:
            print("OS error: {0}".format(err))
            exit(-1)
        else:
            
            data = self.prepare_data()
            writer = csv.writer(storage, delimiter=',')

            for entry in data:
                writer.writerow(entry)
                
            storage.close()

    def txt(self, path=None):
        if path:
            if path.split('.')[-1] != 'txt':
                print("Invalid format. Exiting...")
                exit(-1)
            
            storage_location = path
        else:
            storage_location = self.local_storage

        
        # now the correct path is in storage_location
        try:
            # try to open it
            storage = open(storage_location, 'w')
        except OSError as err:
            print("OS error: {0}".format(err))
            exit(-1)
        else:
            
            data = self.prepare_data()
            
            for entry in data:
                storage.write("[%s] %s - %s\n" % (entry[0], entry[1], entry[2]))

            storage.close()

    def prepare_data(self):
        history = self.getHistory()
        # this is stupid
        services = list(history.keys())

        data = []
 
        # ordered_dates = saver.order_entries_dic(history[sid])
        for sid in history.keys():
            ordered_entries = self.order_entries_dic(history[sid])
            for date, status in ordered_entries:
                data.append([sid, date, status])
                
        return data

    def get_entries(self, sid):
        history = self.getHistory()
        # this is stupid
        services = list(history.keys())

        data = []
 
        # ordered_dates = saver.order_entries_dic(history[sid])
        ordered_entries = self.order_entries_dic(history[sid])
        for date, status in ordered_entries:
            data.append([sid, date, status])
                
        return data

    def order_entries_dic(self, entries):
        final = []
        dates = entries.keys()
        # sort the dates
        dates = sorted(dates, key=lambda date: datetime.datetime.strptime(date, '%x %X'))
        for date in dates:
            final.append([date, entries[date]])

        return final

    def backup(self, path, out_format=None):
        if out_format == None:
            try:
                backup_file = open(path, 'w')
                history = open(self.local_storage, 'r')
            except OSError as err:
                print("OS error: {0}".format(err))
                exit(-1)
            else:
                contents = history.read()
                # do stuff
                backup_file.write(contents)
                backup_file.close()
                history.close()
        elif out_format == 'csv':
            self.csv(path)
        elif out_format == 'txt':
            self.txt(path)
        else:
            print("Unsupported format. Exiting...")
            exit(-1)

    def overwrite_history(self, data):
        try:
            storage = open(self.local_storage, "w")
        except OSError as err:
            print("OS error: {0}".format(err))
            exit(-1)
        else:
            json.dump(data, storage)

    def getHistory(self):
        # try to open the file
        try:
            file = open(self.local_storage, "r")
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