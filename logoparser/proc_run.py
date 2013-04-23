import sys
import time
from urllib import urlretrieve
import BeautifulSoup
import conf.app_settings as LOCAL_SET
from conf.app_settings import ADMIN_LOGGER
from conf.app_settings import APP_LOGGER
import csv
import urlparse
from django.template.defaultfilters import slugify
from job.models import *
import lxml.html.clean
import os
import traceback
import urllib
import urllib2
#f=open('eggs.csv', 'wb')
#spamWriter = csv.writer(f, delimiter='|')
#url='http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?lookuptype=private&region=US&letterIn=a'
#filehandle = urllib2.urlopen(url)
#data = filehandle.read()
#html = unicode(data, errors='ignore')
#doc = BeautifulSoup.BeautifulSoup(lxml.html.clean.clean_html(html))
#
#spamWriter.writerow([e.strip().replace('\"','') for e in result])
import string
lists= [('private','http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?lookuptype=private&region=US&letterIn=%s'),
('public','http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?lookuptype=public&region=US&letterIn=%s')
]
for type,o_url in lists:
    for x in string.lowercase[2:26]:
        
        url=o_url%x        
        while True:
            print url
            filehandle = urllib2.urlopen(url)
            data = filehandle.read()
            html = unicode(data, errors='ignore')
            doc = BeautifulSoup.BeautifulSoup(lxml.html.clean.clean_html(html), convertEntities="html")
            doc=doc.find('div',id='columnLeft')

            tab=doc.findAll('table',{'class':'table'})[0]
            rows= tab.findAll('tr')
            for e in rows:
                comp=e.find('a')
                if comp:
                    source_link= urlparse.urljoin(o_url,comp['href'])
                    company,cr= Company.objects.get_or_create(source_link=source_link)
                    company.name=comp.string.strip()
                    ind=e.findAll('td')[2].string.strip()
                    indus,cr=Industry.objects.get_or_create(name=ind)
                    indus.save()
                    company.type=type
                    company.industry=indus
                    company.save()


            #do parsing
            #look for next
            next= doc.find('a',{'class':'nextBtn'})
            if next:
                 url= 'http://investing.businessweek.com/research/common/symbollookup/'+next['href']                 
            else:
                break
