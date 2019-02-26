#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE:  Visitor abstract class for status checker app
# ===============================

from abc import ABC, abstractmethod


class Visitor(ABC):
    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def visitBitBucket(self, BitBucketStatus): pass

    @abstractmethod
    def visitGitHub(self, GitHubStatus): pass

    @abstractmethod
    def visitSlack(self, SlackStatus): pass

    @abstractmethod
    def visitGitLab(self, GitLabStatus): pass

    @abstractmethod
    def visitGoogleDrive(self, GoogleDriveStatus): pass
