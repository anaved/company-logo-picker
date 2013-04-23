'''
Created on Jan 10, 2012

@author: naved
'''

import ast
from django.core.management import setup_environ
import settings
import traceback
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
import duckduckgo
#
#f=open('top_jobs.txt')
#for e in f.readlines():
#    data= e.split('\t')    
#    try:
#        c,cr= CompanyDuckduckGo.objects.get_or_create(company=data[0])
#        if cr:
#            c.job_count=int(data[2])
#            c.save()
#        
#    except:
#        print data
import time
remove = [
 ' and ',
' for ',
' of ',
' the',
'&amp;',
'.com',
'Company',
'Inc',
'Internship',
'LLC',
'Ltd.',
'The',
        ]
#for compa in CompanyDuckduckGo.objects.filter(result__isnull=True):
#    comp=compa.company
#    for e in remove:
#        comp = comp.replace(e, ' ')
#    try:   
#        print "comp: ",comp 
#        q = comp.lower()
#        r = duckduckgo.query(q)
#        if r.results:    
#            x= r.results[0].__dict__
#            x.pop('icon')
#            x=json.dumps(x)
#            compa.result=x
#            compa.save()
##        print "related", comp,[e.__dict__ for e in r.related]
#        time.sleep(5)
#    except:
#        traceback.print_exc()
#        break
                
#
import urllib
import simplejson
from urlparse import urlparse
for compa in CompanyDuckduckGo.objects.filter(url__isnull=True):
    comp=compa.company
    results=''
    try:
        time.sleep(15)
        for e in remove:
            comp = comp.replace(e, ' ')
        comp=comp.strip()
        query = urllib.urlencode({'q' : comp})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' \
          % (query)
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        url=results[0]['url']
        nt=urlparse(url).netloc    
        compa.url=nt
        compa.save()    
        
    except:
        print comp,url
        traceback.print_exc()
        break
#            