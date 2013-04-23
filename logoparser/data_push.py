# To change this template, choose Tools | Templates
# and open the template in the editor.


import ast
from django.core.management import setup_environ
import settings
import traceback
setup_environ(settings)
from datetime import datetime
import urllib2
#from job.models import  *
#from master.models import  *
import simplejson as  json
from django.core import serializers
import glob
import os
import subprocess
from geo.google.geo_caller import *
import random
import urlparse
import sys

__author__ = "naved"
__date__ = "$31 Jul, 2011 3:40:41 PM$"


def get_location(location):    
    try:
        if len(filter(lambda x:x!='',location.split('-')))>1:
            loc = Locations.objects.filter(in_location=location)
            if not loc:
#                query= format_query(location)
#                time.sleep(3)
#                data= fetch_result(query)
#                state=State.objects.get(name=data['state'])
#                loc,cr= Location.objects.get_or_create(city=data['city'],state=state,lat_lng=Point(float(long),float(lat)))
#                loc = {'city':loc.city,
#                           'state':loc.state,
#                           'lat':loc.latitude,
#                           'long':loc.longitude
#                            }
#                return loc
                 return None
            else:
                loc = loc[0]
                if loc.state:
                    loc = {'city':loc.city,
                           'state':loc.state,
                           'lat':loc.latitude,
                           'long':loc.longitude
                            }
                    return loc
    except:        
        return None
    
def create_major_list(job):
       majors=[]
       major_list=job.major.split('|')
       major_list=filter(lambda x: x!='',major_list)
       for e in major_list:
           m= MajorMap.objects.filter(key=e)
           if m and m[0].major:
               majors.append(m[0].major.name)
               m[0].count=m[0].count+1
               m[0].save()
       return majors

def create_location_list(location):
    location = location.split('|')
    loc_list=[]
    for loc in location:           
        loc=  get_location(loc)
        loc_list.append(loc) if loc else None
    return loc_list
        
def create_dump(f_loc=''):
    jobs = ParsedJobs.objects.filter(is_available=True,is_sent=False,is_valid=True)
    date= datetime.today().__str__().split()[0]
    file = open(f_loc+'jobs_'+date+'.json', 'w')

    count=0
    for e in jobs:
        #TODO clean urls remove reference to indeed or other sites
        data = e.__dict__.copy()
        data.__delitem__('_state')
#        id= data['orig_id']=data['id']
        data.__delitem__('id')
#        JobScoreBack.objects.get_or_create(**data)
        major=create_major_list(e)
        location=create_location_list(data['location'])
#        data.__delitem__('orig_id')
        #DELETE PARSER RELATED FIELDS
        data.__delitem__('is_sent')
        data.__delitem__('manual_done')
        data.__delitem__('is_valid')
        data.__delitem__('is_available')
        data.__delitem__('manual_by')
        data.__delitem__('timestamp')
        data['posting_date'] = data["posting_date"].__str__()
        if major and location and data['company']:
                data['major'] = major
                data['location'] = location
                
                count+=1
                file.write(json.dumps(data)+"\n");
                if e.manual_done==True:
                    e.is_sent=True
                e.save()
        else:
            print "FAILED: ","id: ",e.id," major: ",major," new location : ",location," actual location: ",data['location']," company: ",data['company']
            e.is_valid=False
            e.save()
    print "WRITTEN: ",count
    # if saturday
    if datetime.today().weekday()==5:
        print "WEEK ENDED, MARKING ALL JOBS AS DONE "
        jobs.update(is_sent=True)
    file.close()
    return file.name

def push_dump(filename):
    cmd=['fab','push_job_data:'+filename]
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    out,err = p.communicate('hello world')
    print out,err    

if __name__ == "__main__":
   print "creating dump"
   file= create_dump('dump/')
   print "pushing file"
   push_dump(file)
