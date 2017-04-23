#!/usr/bin/python2.7
import paramiko
import sys
import os
import time
import re

        # # # # # # # ## # # ## # ## # # ## # ## # ## # ## # # ##  # # # ## # 
a = {"version_string": "1.16.1689", "build_number": "108718", "pretty_name": "dvr_GA", "flavor_id": "113420", "branch": "dvr_GA", "build_flavor": "release"}# 
# 

    
        
        #stdin, stdout, stderr=client.exec_command('cat /etc/version.json')
        #data3 = stdout.read()
        #line = data3.split('\n')
        #line = data3.split(',')
b = str(a)
line = b.split(',')
print line
print line[0]
print line[0][1 :]
print line[1]
# regexp = re.compile (r'version[_string]')
regexp = re.compile (r'\d+.\d+.\d+




')        
if regexp.search(b):
#    regexp.findall(b)
        
                
            
#           f = open ("report1.txt", "a+")
     #       f.write(lin + "\n")
    c = regexp.findall(b)
    print 'matched'
    print b
    print c
        #print (line)
        
        
        
        
        # # # # ## # # # ## # # ## # # ## # # # ## ## # # ## # # # # ## # ## # ## # ## # 
        
        
        
      
           

    