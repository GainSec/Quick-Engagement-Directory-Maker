import subprocess
import argparse
import re
import os
import pathlib

parser = argparse.ArgumentParser()

parser.add_argument('--e', default='ENGAGEMENT-TYPE', help='Engagement Type')
parser.add_argument('--c', default='CLIENT-NAME', help='Client Name')
parser.add_argument('--p', default='PROJECT-NAME', help='Project Name')
parser.add_argument('--r', default='~/Desktop/Engagements/', help='Custom Engagement Root')

args = parser.parse_args()

e = args.e
r = args.r
c = args.c
p = args.p

EngagementType = e
ClientName = c
ProjectName = p
EngagementRoot = os.path.expanduser(r)
EngagementDirectoryPath = ''

def EngagementDirectoryCreate():
    EngagementDirectoryPath = (EngagementRoot + EngagementType + '/' + ClientName + '/' + ProjectName + '/')
    path = pathlib.Path(EngagementDirectoryPath)
    path.mkdir(parents=True, exist_ok=True)
    print("Engagment Root Path Created: ", EngagementDirectoryPath)
    return EngagementDirectoryPath


def CreateEngagementSubDirectories(EngagementDirectoryPath):
    SubDirectoryList = ['Screenshots', 'Notes', 'Exports-Downloads', 'Template-Docs', 'Payloads', 'PRJ', 'Errors', 'Output', 'Report']
    for line in SubDirectoryList:
        SubDir = (EngagementDirectoryPath + line)
        path = pathlib.Path(SubDir)
        path.mkdir(parents=True, exist_ok=True)
        print('The ', SubDir , ' SubDirectory was made')

def Banner():
    print("Quick Engagement Directory Creation Script (Q.E.D.C.S)")
    print("By Jon Gaines (@GainSec) - Managing Security Consultant @NetSPI")
    print(" ")
    print("Example: ./qedcs.py")
    print("Will create the Engagement Data Root Directory at: ")
    print("/Users/Username/Desktop/Engagements/ENGAGEMENT-TYPE/CLIENT-NAME/PROJECT-NAME/")
    print("OR")
    print("C:\\Users\\Username\\Desktop\\Engagements\\ENGAGEMENT-TYPE\\CLIENT-NAME\\PROJECT-NAME")
    print(" ")
    print("Better Example: ./qedcs.py --e WEB --c GAINSEC --p BLOG")
    print("Which will create the Engagement Data Root at: ")
    print("~/Desktop/WEB/GAINSEC/BLOG")
    print("OR")
    print("C:\\Users\\Username\\Desktop\\Engagements\\WEB\\GAINSEC\\BLOG")
    print(" ")


def Main():
    Banner()
    ActualEngagementDirectoryPath = EngagementDirectoryCreate()
    EngagementDirectoryCreate()
    CreateEngagementSubDirectories(ActualEngagementDirectoryPath)


Main()