# To change this template, choose Tools | Templates
# and open the template in the editor.


import ast
from django.core.management import setup_environ
import settings
import traceback
from inspect import Traceback
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
    return company

#result= ParsedJobs.objects.filter(company__icontains='disney').distinct('company').values('company')
#ofile=open('top_jobs.txt')
#for z in ofile.readlines():
#    e=z.strip()
##    e=clean(e)                           
#    logos=CompanyLogo.objects.filter(company__contains=e.strip()+' ')
#    for f in logos:        
#        logo=f.company
#        for x in remove:   
#            try:                     
#                logo=logo.replace(x,' ')
#                if re.search(" "+e," "+logo) or (len(e.strip())>3 and re.search(e,logo)):
#                    print e,':',logo
#            except:                    
#                pass
            
#        try:
#            e=e.strip()
#            logo=logo.strip()        
#                
#            k,cr=KeyLogo.objects.get_or_create(key=z.strip())
#            k.logo.add(f)
#            k.save()
#        except:
#            traceback.print_exc()
#            break

#import imghdr
#import shutil        
#from PIL import Image
#logos=CompanyLogo.objects.all()
#for e in logos:
#    try:
#        f=open(e.logo_location)        
#        t= imghdr.what(f)
#        print Image.open(f).size,e.company,t,e.logo_location
##        ext= e.biglogo_location.split('.')[-1]
##        if  t=='gif' and ext=='png':
##            np=e.biglogo_location.split('.')[0]+'.gif'
##            print np            
##            shutil.copy(e.biglogo_location, np)
##            e.biglogo_location=np
##            e.save()
#        f.close()
#    except:
#        pass    
        
from PIL import Image           
ofile=open('top_jobs.txt')
#f=open('logos.txt','w')
for z in ofile.readlines():
    e=z.strip()
    comps=Company.objects.filter(name__contains=e+' ')
    for x in comps:                           
        logos=CompanyLogo.objects.filter(company__contains=x.name.strip())        
        if logos:
            for f in logos:                
                logo=f.company                                  
                try:                    
                    if re.search(" "+x.name," "+logo) or (len(x.name.strip())>3 and re.search(x.name,logo)):
                        print "INDIVIDUAL:", x.name,':',logo
                except:                    
                    pass        
        else:
            logos=CompanyLogo.objects.filter(company__contains=e+' ')
            for f in logos:        
                logo=f.company                   
                try:                   
                    if re.search(" "+e," "+logo) or (len(e.strip())>3 and re.search(e,logo)):
                        fi=open(f.logo_location)
                        si=logo,Image.open(fi).size                        
                        print "GROUP : ", e,':',x.name,':',si[1],':',f.logo_location
                            
                        fi.close()
                except:                    
                    pass                    