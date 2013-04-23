#! /usr/bin/python

import ast
from django.core.management import setup_environ
import settings
import traceback
from data_filter import companies
setup_environ(settings)
from datetime import datetime
import urllib2
from job.models import  *
import simplejson as  json
from django.core import serializers
import glob
import os
import subprocess
import re
import random
import urlparse
import sys

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="naved"
__date__ ="$23 Aug, 2011 6:13:51 PM$"

print "NAVED"
logos=CompanyLogo.objects.all()
for logo in logos:
   try:
     comp= logo.company 
     p=  ParsedJobs.objects.filter(company__icontains=comp)
     print "NAVED",p

   except:
       pass