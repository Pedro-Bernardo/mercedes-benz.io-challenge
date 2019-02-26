#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE: SlackStatus class
# ===============================

from core.Status import Status

class SlackStatus(Status):
    ID = "slack"
    def __init__(self, name, url):
        super().__init__(name, url)
        self.up_string = 'Slack is up and running'

    def __str__(self):
        return self.__class__.__name__

    def accept(self, Visitor):
        return Visitor.visitSlack(self)

    def getUpString(self):
        return self.up_string