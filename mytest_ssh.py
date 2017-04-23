#!/usr/bin/python2.7
import paramiko
import sys
import os
import time
import re

deviceIp = "192.168.1.102"
deviceIPs = ["192.168.1.102"]
# deviceIPs = ["192.168.1.103","192.168.202.152","192.168.203.152","192.168.204.152"]
user = "root"
passwd = "verizon123"

for device in deviceIPs:

    client = None
    f = None
    f2 = None
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        #client.connect("192.168.1.19",username="henry", password="boot12")
        client.connect(device,username= user, password= passwd)
    
                
        f = open (device + "-report1.txt", "a+")  
        f2 = open ("segment_info.txt", "a+") 
        print("#### Test: Device under Test  ####")  
        print(device) 
        print("#### Test: Dvr_SOAK_test_start.py  ####")
        print("#### Test: test start  ####")
        print("#### Test1: Get DVR app version and client build ####")
#       f = open ("report1.txt", "a+") 
        f.write  ("############ Test: test start  ############## \n")     
        f.write  ("#### Test1: Get DVR app version and client build #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('cat /data/app/Version.json')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        stdin, stdout, stderr=client.exec_command('cat /etc/version.json')
        a = stdout.read()
 ##       data3 = stdout.read()
 ##       line = data3.split('\n')
 ##       for lin in line:
#           f = open ("report1.txt", "a+")
 ##             f.write(lin + "\n")
  ##            print (lin)
        #print (line)

        # # # # # # # ## # # ## # ## # # ## # ## # ## # ## # # ##  # # # ## # 
##a = {"version_string": "1.16.1689", "build_number": "108718", "pretty_name": "dvr_GA", "flavor_id": "113420", "branch": "dvr_GA", "build_flavor": "release"}# 
# 

    
        
        #stdin, stdout, stderr=client.exec_command('cat /etc/version.json')
        #data3 = stdout.read()
        #line = data3.split('\n')
        #line = data3.split(',')
        b = str(a)
        l = str(a)
        line = b.split(',')
        print line
        print line[0]
        print line[0][1 :]
        print line[1]
        print '####'
        print l
# regexp = re.compile (r'version[_string]')
        regexp = re.compile (r'\d+.\d+.\d+')        
        if regexp.search(b):
#    regexp.findall(b)
        
                
            
#           f = open ("report1.txt", "a+")
     #       f.write(lin + "\n")
            c = regexp.findall(b)
            print 'matched'
            print b
            print c
        
        line = l.split(',')   
        regexp = re.compile (r'version\w+')
        if regexp.search(l):
           d = regexp.findall(l) 
           print 'matched'
           print l
           print d
           
           print l
           print d
        #print (line)
           print l
           print d 
        
        
        
        # # # # ## # # # ## # # ## # # ## # # # ## ## # # ## # # # # ## # ## # ## # ## # 
    except:
        print "Exception"
    finally:
        if f2 is not None:
            f2.close()
        if f is not None:
            f.close()
        if client is not None:
            client.close()      
        
        
      
           

    
