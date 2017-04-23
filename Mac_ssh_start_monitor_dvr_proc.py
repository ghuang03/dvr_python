#!/usr/bin/python2.7
import paramiko
import sys
import os
#deviceIp = "192.168.200.158"
deviceIp = "192.168.1.103"
deviceIPs = ["192.168.1.103","192.168.1.152"]
user = "root"
passwd = "verizon123"

for device in deviceIPs:

    client = None
    f = None
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        #client.connect("192.168.1.19",username="henry", password="boot12")
        client.connect(device,username= user, password= passwd)
            
        f = open (device + "-monitor.txt", "a+")      
       
        print("#### Test1: Start monitoring dvr_client ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test1: Start monitoring dvr_client  #### \n")       
 #       stdin, stdout, stderr=client.exec_command('mv  /hd/data/cpu_mem_monitor_log /hd/data/cpu_monitor_log_old')        
        stdin, stdout, stderr=client.exec_command('cd /hd/data;./cpu_mem_monitor &')
        stdin, stdout, stderr=client.exec_command('cd /hd/data;ls -l')
 #       stdin, stdout, stderr=client.exec_command('pwd')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        
        print("#### Test2: Start monitoring all process cpu usages ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test2: Start monitoring all process cpu usages #### \n")                
        stdin, stdout, stderr=client.exec_command('cd /hd/data;./total_cpu_monitor &')
        stdin, stdout, stderr=client.exec_command('cd /hd/data;ls -l')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
 
            
        print("#### Test3: Check and verify the process are running ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test3: Check and verify the process are running #### \n")
                
        stdin, stdout, stderr=client.exec_command(' ps -auxf | grep cpu')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
    except:
        print "Exception"
    finally:
        if f is not None:
            f.close()
        if client is not None:
            client.close()

