#!/usr/bin/env python3
# ===============================
# AUTHOR: Pedro Bernardo
# CREATE DATE: 23 Feb 2019
# PURPOSE: StatusChecker class, Visitor implementation
# ===============================

from core.parsers import *
from core.Visitor import Visitor
from socket import timeout
import urllib.request
import urllib.error
import os

class StatusChecker(Visitor):

    def visitBitBucket(self, BitBucketStatus): 
        try:
            html = urllib.request.urlopen(BitBucketStatus.getURL(), timeout=10).read().decode('utf-8')

        except (urllib.error.HTTPError, urllib.error.URLError) as error:
            print("%s is unavailable" % BitBucketStatus.getURL())
            BitBucketStatus.updateStatus('status unavailable')
            return BitBucketStatus.display_status()
            
        except timeout:
            print('socket timeout: %s', url)
            BitBucketStatus.updateStatus('could not connect')
            return BitBucketStatus.display_status()
        
        parser = BitBucketParser()
        parser.feed(html)
        status = parser.getStatus()

        if BitBucketStatus.getUpString() in status and status != "":
            BitBucketStatus.updateStatus('up')
        else:
            BitBucketStatus.updateStatus('down')
    
        return BitBucketStatus.display_status()
        
    def visitSlack(self, SlackStatus): 
        try:
            html = urllib.request.urlopen(SlackStatus.getURL(), timeout=10).read().decode('utf-8')

        except (urllib.error.HTTPError, urllib.error.URLError) as error:
            print("%s is unavailable" % SlackStatus.getURL())
            SlackStatus.updateStatus('status unavailable')
            return SlackStatus.display_status()

        except timeout:
            print('socket timeout: %s', url)
            SlackStatus.updateStatus('could not connect')
            return SlackStatus.display_status()
        
        parser = SlackParser()
        parser.feed(html)
        status = parser.getStatus()

        if SlackStatus.getUpString() in status and status != "":
            SlackStatus.updateStatus('up')
        else:
            SlackStatus.updateStatus('down')

        return SlackStatus.display_status()

    def visitGitLab(self, GitLabStatus): 
        try:
            html = urllib.request.urlopen(GitLabStatus.getURL(), timeout=10).read().decode('utf-8')

        except (urllib.error.HTTPError, urllib.error.URLError) as error:
            print("%s is unavailable" % GitLabStatus.getURL())
            GitLabStatus.updateStatus('status unavailable')
            return GitLabStatus.display_status()
            
        except timeout:
            print('socket timeout: %s', url)
            GitLabStatus.updateStatus('could not connect')
            return GitLabStatus.display_status()
            
        
        parser = GitLabParser()
        parser.feed(html)
        status = parser.getStatus()

        if GitLabStatus.getUpString() in status and status != "":
            GitLabStatus.updateStatus('up')
        else:
            GitLabStatus.updateStatus('down')

        return GitLabStatus.display_status()

    def visitGoogleDrive(self, GoogleDriveStatus): 
        pass

    def visitGitHub(self, GitHubStatus): 
        try:
            html = urllib.request.urlopen(GitHubStatus.getURL(), timeout=10).read().decode('utf-8')

        except (urllib.error.HTTPError, urllib.error.URLError) as error:
            print("%s is unavailable" % GitHubStatus.getURL())
            GitHubStatus.updateStatus('status unavailable')
            return GitHubStatus.display_status()
            
        except timeout:
            print('socket timeout: %s', url)
            GitHubStatus.updateStatus('could not connect')
            return GitHubStatus.display_status()
            
        
        parser = GitHubParser()
        parser.feed(html)
        status = parser.getStatus()

        if GitHubStatus.getUpString() in status and status != "":
            GitHubStatus.updateStatus('up')
        else:
            GitHubStatus.updateStatus('down')

        return GitHubStatus.display_status()
