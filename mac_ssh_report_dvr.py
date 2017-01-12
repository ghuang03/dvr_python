#!/usr/bin/python2.7
import paramiko
import sys
import os
#deviceIp = "192.168.200.158"
deviceIp = "192.168.1.153"
deviceIPs = ["192.168.1.153","192.168.202.152","192.168.203.152","192.168.204.152"]
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
    
                
        f = open (device + "-report_test_start.txt", "a+")      
       
        print("#### Test1: Get DVR app version and client build ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test1: Get DVR app version and client build #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('cat /data/app/Version.json')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        stdin, stdout, stderr=client.exec_command('cat /etc/version.json')
        data3 = stdout.read()
        line = data3.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        #print (line)
        
        
        print("#### Test2: Get DVR system uptime ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test2: Get DVR system uptime  #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('uptime -s')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        stdin, stdout, stderr=client.exec_command('uptime -p')
        data3 = stdout.read()
        line = data3.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        #print (line)
        
        print("#### Test3: Check archieved logs for app crashes ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test3: Check archieved logs for app crashes #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('ls -larth /hd/data/logs/archived | tail -n 5')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        stdin, stdout, stderr=client.exec_command('date')
        data3 = stdout.read()
        line = data3.split('\n')
#       f = open ("report1.txt", "a+")
        f.write("#date")
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        print("#### Test4: Record dvr_client CPU, Mem usages ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test4: Record dvr_client CPU, Mem usages #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('ps -C dvr_client -o %cpu,%mem,cmd ')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        print("#### Test5: Record total CPU usage ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test5: Record total CPU usage #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('mpstat ')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
        
        print("#### Test6: Record Hard Drive spaces under /hd/data/www ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test6: Record Hard Drive spaces under /hd/data/www #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('ls -larth /hd/data/www ')
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

