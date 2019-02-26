#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE: GoogleDriveStatus class
# ===============================

from core.Status import Status

class GoogleDriveStatus(Status):
    ID = "googledrive"
    def __init__(self, name, url):
        super().__init__(name, url)
        self.up_string = 'All Systems Operational'

    def __str__(self):
        return self.__class__.__name__


    def accept(self, Visitor):
        return Visitor.visitGoogleDrive(self)

    def getUpString(self):
        return self.up_string