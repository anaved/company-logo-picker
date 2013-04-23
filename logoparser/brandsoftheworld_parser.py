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
import BeautifulSoup
from django.template.defaultfilters import slugify
import os
import re
from urllib import urlretrieve
import urllib2

burl='http://www.brandsoftheworld.com/logos/countries/us?page=%d'
for e in range(75,421):
#and here is the new show
    url=burl%e
    try:
        filehandle = urllib2.urlopen(url)
        data = filehandle.read()
        html = unicode(data, errors='ignore')
        doc = BeautifulSoup.BeautifulSoup(lxml.html.clean.clean_html(html))
        logos=doc.find('ul',{'class':'logos'})
        logos=logos.findAll('img',{'class':'image'})
        for imagez in logos:
            try:
                img=imagez['src']
                company=imagez['alt'].replace('Logo of ','')
                logo,cr= CompanyLogo.objects.get_or_create(source_link=img)
                logo.company=company
                company=slugify(company)
                path='/home/naved/NetBeansProjects/LogoParser/LogoParser/images/'+company
                if not os.path.exists(path):
                    os.makedirs(path)
                filename= "_bow.".join(img.split('/')[-1].split('.'))
                outpath = os.path.join(path, filename)
                urlretrieve(img, outpath)
                if not logo.logo_location:
                    logo.logo_location=outpath
                logo.save()
                print company
                time.sleep(3)
            except:
                print "HIDDEN:",img
    except:
        print "ERROR:",url
#yeah baby 
#there you go