#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Status command
# ===============================

from core.commands.Command import Command
from core.Saver import Saver
import datetime

class DoStatus(Command):
    ID = 'status'
    HELP = 'Summarizes data and displays it in a table-like fashion'
    def __init__(self, service_list, args):
        self._services = service_list
        self._args = args
    
    def __str__(self):
        return self.__class__.__name__

    def execute(self):
        def mttf(entries):
            n_runs = 0
            durations = []
            in_run = False
            for e in entries:
                date = e[1]
                status = e[2]
                # if its the first of a run
                if not in_run and status != 'down':
                    in_run = datetime.datetime.strptime(date, "%x %X")
                    durations.append(in_run)
                    n_runs += 1
                # if it's in the middle of a run
                elif status == 'up':
                    durations[n_runs - 1] = datetime.datetime.strptime(date, "%x %X") - in_run
                # if it's the end of a run
                elif in_run and status != 'up':
                    in_run = False

            if n_runs == 1:
                return None
            else:
                sum_durations = datetime.timedelta(seconds=0)
                for d in durations:
                    sum_durations = d + sum_durations
                
                return sum_durations/n_runs
        
        def uptime(entries):
            n_runs = 0
            durations = []
            in_run = False
            for e in entries:
                date = e[1]
                status = e[2]
                # if its the first of a run
                if not in_run and status != 'down':
                    in_run = datetime.datetime.strptime(date, "%x %X")
                    durations.append(in_run)
                    n_runs += 1
                # if it's in the middle of a run
                elif status == 'up':
                    durations[n_runs - 1] = datetime.datetime.strptime(date, "%x %X") - in_run
                # if it's the end of a run
                elif in_run and status != 'up':
                    in_run = False

            uptime_val = datetime.timedelta(seconds=0)
            for d in durations:
                uptime_val += d
            
            return uptime_val

        saver = Saver()
        history = saver.getHistory()

        # print table header
        print("| service       | uptime        | mttf          |")
        print("+---------------+---------------+---------------+")
        space = 14
        
        template = "| {}| {}| {}|"
        for sid in history.keys():
            upt_t = str(int(uptime(saver.get_entries(sid)) / datetime.timedelta(minutes=1))) + "min"
            if mttf(saver.get_entries(sid)) != None:
                mttf_t = str(int(mttf(saver.get_entries(sid)) / datetime.timedelta(minutes=1))) + "min"
            else:
                mttf_t = 'infinite'

            # assuming service id is always less than 16 characters long
            print(template.format(sid.ljust(space, ' '), upt_t.ljust(space, ' '), mttf_t.ljust(space, ' ')))
            
        
        #datetime.now().strftime("%x %X"), self.last_status)


    
