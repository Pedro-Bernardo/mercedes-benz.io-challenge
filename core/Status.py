#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE: GoogleDriveStatus class
# ===============================

from abc import ABC, abstractmethod
from core.Service import Service
from datetime import datetime


class Status(Service):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.last_status = None

    @abstractmethod
    def accept(self, Visitor): pass

    def display_status(self):
        if self.last_status != None:
            return "[%s] %s - %s" % (self.ID, datetime.now().strftime("%x %X"), self.last_status)
        else:
            return "[%s] no status." % (self.ID)
        

    def getURL(self):
        return self.url
    
    def getName(self):
        return self.name
    
    def updateStatus(self, status):
        self.last_status = status

    def getLastStatus(self):
        return self.last_status
