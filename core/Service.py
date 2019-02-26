#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Service abstract class for status checker app
# ===============================

from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def accept(self, Visitor): pass