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


def get_big_logo(url):
    filehandle = urllib2.urlopen(url)
    data = filehandle.read()
    html = unicode(data, errors='ignore')
    doc = BeautifulSoup.BeautifulSoup(lxml.html.clean.clean_html(html))
    tab=doc.find('table',id="main-table")
    tab=tab.find('td',{'class':'labelText','align':'center'})
    a=tab.findAll('a')
    company_name=a[1].string.strip()
    img= a[0].img['src']
    biglogopath= urlparse.urljoin(url,img)    
    return company_name,biglogopath


url='http://www.goodlogo.com/a-z'
filehandle = urllib2.urlopen(url)
data = filehandle.read()
html = unicode(data, errors='ignore')
doc = BeautifulSoup.BeautifulSoup(html)
tab=doc.findAll('p',{'class':'expired'})
imgs= doc.findAll('span',{'class':'clickList'})
for imagez in imgs:
        img= imagez.a['onmouseover']
        img= re.search('\".*\"',img)
        if img:            
            biglogo=imagez.a['href']
            biglogo= urlparse.urljoin(url,biglogo)
            logo,cr= CompanyLogo.objects.get_or_create(source_link=biglogo)
            company,biglogo=get_big_logo(biglogo)
            logo.company=company
            company=slugify(company)
            img='http://www.goodlogo.com'+img.group().replace('"','')            
            filename = (company)+"."+img.split('.')[-1]
            path='/home/naved/NetBeansProjects/LogoParser/LogoParser/images/'+company
            if not os.path.exists(path):
                os.makedirs(path)
            outpath = os.path.join(path, filename)
            urlretrieve(img, outpath)
            logo.logo_location=outpath
            filename=biglogo.split('/')[-1].replace('.','_big.')
            outpath = os.path.join(path, filename)
            urlretrieve(biglogo, outpath)            
            logo.biglogo_location=outpath
            logo.save()
            print company
            time.sleep(3)