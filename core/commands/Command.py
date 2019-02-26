#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Command abstract class for status checker app
# ===============================

from abc import ABC, abstractmethod

class Command(ABC):
    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def execute(self): pass
    