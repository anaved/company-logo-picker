import os
import glob
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib import files, console
from fabric import utils
from fabric.decorators import hosts
from fabric.api import env
import time


env.key_filename = '/home/naved/main-kp.pem'
env.user = 'root'
env.hosts = ['ec2-107-20-48-196.compute-1.amazonaws.com']
env.activate='source /home/django/domains/lazyzach.com/lazyzach.com/bin/activate'
INSTANCE_ID=None
#filename = "dump/jobs_2011-08-08.json"

def push_job_data(filename):
    filepath="/var/tmp/"+filename.split("/")[-1]
    print "putting file :",filename," at :",filepath
    put(filename, filepath)
    with cd('/home/django/domains/lazyzach.com/lazyzach/'):
        with prefix(env.activate):
            print "running file: ",filepath
            run('python %s %s'%('push_data.py ',filepath,))


#def create_env():
#       print "creating env"
#       result= local('ec2-run-instances -C /home/naved/ec2/cert-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem  -K /home/naved/ec2/pk-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem  -t m1.small -z us-east-1b ami-161ce97f',capture=True)
#       instance_details=result.split()
#       print  "START: ",instance_details
#       global INSTANCE_ID
#       INSTANCE_ID= instance_details[5]
#       global PUB_DNS
#       while True:
#            time.sleep(120)
#            status=local('ec2-describe-instances -C /home/naved/ec2/cert-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem  -K /home/naved/ec2/pk-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem %s'%INSTANCE_ID,capture=True)
#            print "STATUS: ",status.split()
#            if status.split()[7].strip()!='pending':
#                PUB_DNS=status.split()[7]
#                break
#       env.hosts = [PUB_DNS]
#       env.key_filename = '/home/naved/main-kp.pem'
#       env.user = 'root'
#
#
#def get_locs(prog_file,in_file):
#    print 'getting locations'
#    print prog_file,in_file
#    prog_name=prog_file.split('/')[-1]
#    in_name=in_file.split('/')[-1]
#    print "Setting"
#    put(prog_file, '/var/tmp/'+prog_name)
#    put(in_file, '/var/tmp/'+in_name)
#    print "Running"
#    with cd('/var/tmp/'):
#            run('python %s %s'%(prog_name,in_name))
#    print "Getting"
#    get('/var/tmp/'+in_name+'.out','loc_out/'+in_name+'.out')
#    print 'done'
#    stop_s=local('ec2-terminate-instances -C /home/naved/ec2/cert-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem  -K /home/naved/ec2/pk-CESXUSEEYWUCFOBXWY2RVYFNGQPK6LI4.pem %s'%INSTANCE_ID,capture=True)
#    print "STOP: ",stop_s.split()
#
#def test(data,tata):
#    print "hello I am listening :"+data+tata
