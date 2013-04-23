# To change this template, choose Tools | Templates
# and open the template in the editor.


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

__author__ = "naved"
__date__ = "$31 Jul, 2011 3:40:41 PM$"

#logos=CompanyLogo.objects.all()
#companies=set([])
#for logo in logos:
#   try:
#     comp= logo.company 
#     result=  ParsedJobs.objects.filter(company__icontains=comp)          
#     for p in result:         
#         x=p.company.split()         
#         if logo.company in x:
#             a= [logo.company,p.company,logo.logo_location]
#             print a
#             companies.add(a)
#   except:
#       pass

remove=['Inc.' ,
'Industries' ,
' of ' ,
'The' ,
'&amp;' ,
'Center' ,
' for ' ,
'Group' ,
' and ' ,
'Health' ,
'Corporation' ,
'Corp' ,
'LLC' ,
'-' ,
'Operations',
'Information',
'International' ,
'Inc' ,
'Company' ,
'National' ,
'Services' ,
'Internship' ,
'Hospital' ,
'University' ,
'Foundation' ,
'New' ,
'Institute' ,
' the' ,
'City' ,
'Association' ,
'Solutions' ,
'Systems' ,
'Network' ,
'America' ,
'Public' ,
'Marketing' ,
'Communications' ,
'Global' ,
'Management' ,
'Entertainment' ,
'Financial' ,
'System' ,
'Council' ,
'Research' ,
'Society' ,
'Technology' ,
'Associates' ,
'Bank' ,
'Productions' ,
'Partners' ,
'Trust' ,
'Investment' ,
'Ltd.' ,
'.com' ,
'College' ,
'School' ,
'Travel',
'Services',
'Service',
'Company',
',',
'  ',
]
import difflib

def clean(company):
    for x in remove:        
        company=company.replace(x,' ')
    return company.strip()
x=set([])
#ofile=open('top_jobs.txt')
#for z in ofile.readlines():
#    x.add(clean(z))
#for e in x:
#    print e


#result= ParsedJobs.objects.filter(company__icontains='disney').distinct('company').values('company')
ofile=open('top_jobs.txt')
for z in ofile.readlines():
    e=z.strip()
    e=clean(e)                           
    logos=Company.objects.filter(name__startswith=e.strip()+' ')
    for f in logos:        
        logo=f.name
        for x in remove:   
            try:     
                logo=logo.replace(x,' ')
            except:                    
                pass
            
        try:
            e=e.strip()
            logo=logo.strip()
#            ratio=difflib.SequenceMatcher(None, e, logo).ratio()
#                if ratio>=0.7:
                #KeyMatch.objects.get_or_create(key_company=e,value_company=z['company'],key_logo=logo,value_logo=f['company'],matchp=ratio)                            
            k,cr=KeyCompany.objects.get_or_create(key=z.strip())
            k.company.add(f)
            k.save()
        except:
            traceback.print_exc()
            break
        
        
            
        
    