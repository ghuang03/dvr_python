#!/usr/bin/python2.7
import paramiko
import sys
import os
import time
#deviceIp = "192.168.200.158"
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
        
        print("#### Test3.1: Check archieved logs ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test3.1: Check archieved logs #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('ls -larth /var/logs/archived | tail -n 15')
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
            
            
        print("#### Test3.2: Check app crashes ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test3.2: Check app crashes #### \n")
        
        
        stdin, stdout, stderr=client.exec_command('ls -larth /hd/data/testlog')
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
        
        
        stdin, stdout, stderr=client.exec_command('sar -u 2 5')
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
            
        
        stdin, stdout, stderr=client.exec_command('df -h | grep /hd/data/ ')
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
         
        
        print("#### Test7: Record multicast channel spaces under /hd/data/www and recording activity ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test7: Record multicast channel spaces under /hd/data/www #### #### \n")
        
           
        print("#### Test7.1: Record multicast channel spaces under /hd/data/www ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test7.1: Record multicast channel spaces under /hd/data/www #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('du -sh ./KGODT/ ./KPIXDT/ ./KTVUDT/ ./KMTPDT/  ')
        time.sleep(6) 
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)

        print("#### Test7.2: Record multicast channel recording activity under /hd/data/www ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test7.2: Record multicast channel recording activity under /hd/data/www #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('ls -d /hd/data/www/*/*/ -altrh |tail -n12')
        time.sleep(6) 
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
            
        stdin, stdout, stderr=client.exec_command('date')
        time.sleep(6) 
        data2 = stdout.read()
        line = data2.split('\n')
        for lin in line:
#           f = open ("report1.txt", "a+")
            f.write(lin + "\n")
            print (lin)
            
            
        print("#### Test8: Record multicast KGODT channel segments ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test8: Record multicast KGODT channel segments #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KGODT | grep 2e96.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KGODT_2e96.m4a_start = "+data2 + "\n")
        f2.write("KGODT_2e96.m4a_start = "+data2 + "\n")
        print ("KGODT_2e96.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KGODT | grep 5e192.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KGODT_5e192.m4a_start = "+data2 + "\n")
        f2.write("KGODT_5e192.m4a_start = "+data2 + "\n")
        print ("KGODT_5e192.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KGODT | grep 01MBt.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KGODT_01MBt.m4v_start = "+data2 + "\n")
        f2.write("KGODT_01MBt.m4v_start = "+data2 + "\n")
        print ("KGODT_01MBt.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KGODT | grep 1MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KGODT_1MBm.m4v_start = "+data2 + "\n")
        f2.write("KGODT_1MBm.m4v_start = "+data2 + "\n")
        print ("KGODT_1MBm.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KGODT | grep 5MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KGODT_5MBm.m4v_start = "+data2 + "\n")
        f2.write("KGODT_5MBm.m4v_start = "+data2 + "\n")
        print ("KGODT_5MBm.m4v_start = "+data2 + "\n")  
        
        print("#### Test9: Record multicast KPIXDT channel segments ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test9: Record multicast KPIXDT channel segments #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KPIXDT | grep 2e96.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KPIXDT_2e96.m4a_start = "+data2 + "\n")
        print ("KPIXDT_2e96.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KPIXDT | grep 5e192.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KPIXDT_5e192.m4a_start = "+data2 + "\n")
        print ("KPIXDT_5e192.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KPIXDT | grep 01MBt.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KPIXDT_01MBt.m4v_start = "+data2 + "\n")
        print ("KPIXDT_01MBt.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KPIXDT | grep 1MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KPIXDT_1MBm.m4v_start = "+data2 + "\n")
        print ("KPIXDT_1MBm.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KPIXDT | grep 5MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KPIXDT_5MBm.m4v_start = "+data2 + "\n")
        print ("KPIXDT_5MBm.m4v_start = "+data2 + "\n") 
         
         
        print("#### Test10: Record multicast KTVUDT channel segments ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test10: Record multicast KTVUDT channel segments #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KTVUDT | grep 2e96.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KTVUDT_2e96.m4a_start = "+data2 + "\n")
        print ("KTVUDT_2e96.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KTVUDT | grep 5e192.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KTVUDT_5e192.m4a_start="+data2 + "\n")
        print ("KTVUDT_5e192.m4a_start="+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KTVUDT | grep 01MBt.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KTVUDT_01MBt.m4v_start = "+data2 + "\n")
        print ("KTVUDT_01MBt.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KTVUDT | grep 1MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KTVUDT_1MBm.m4v_start = "+data2 + "\n")
        print ("KTVUDT_1MBm.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KTVUDT | grep 5MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KTVUDT_5MBm.m4v_start = "+data2 + "\n")
        print ("KTVUDT_5MBm.m4v_start = "+data2 + "\n") 
         
         
         
        print("#### Test11: Record multicast KMTPDT channel segments ####")
#       f = open ("report1.txt", "a+")      
        f.write  ("#### Test11: Record multicast KMTPDT channel segments #### #### \n")
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KMTPDT | grep 2e96.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KMTPDT_2e96.m4a_start="+data2 + "\n")
        print ("KMTPDT_2e96.m4a_start="+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KMTPDT | grep 5e192.m4a | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KMTPDT_5e192.m4a_start = "+data2 + "\n")
        print ("KMTPDT_5e192.m4a_start = "+data2 + "\n")   
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KMTPDT | grep 01MBt.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KMTPDT_01MBt.m4v_start = "+data2 + "\n")
        print ("KMTPDT_01MBt.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KMTPDT | grep 1MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KMTPDT_1MBm.m4v_start = "+data2 + "\n")
        print ("KMTPDT_1MBm.m4v_start = "+data2 + "\n")  
        
        stdin, stdout, stderr=client.exec_command('find /hd/data/www/KMTPDT | grep 5MBm.m4v | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("KMTPDT_5MBm.m4v_start = "+data2 + "\n")
        print ("KMTPDT_5MBm.m4v_start = "+data2 + "\n") 
         
         
        stdin, stdout, stderr=client.exec_command('find /var/log/oncueapp | grep Missing | wc -l')
        data2 = stdout.read()
        line = data2.split('\n')
#       for lin in line:
#           f = open ("report1.txt", "a+")
        f.write("Missing_Segment_File_start = "+data2 + "\n")
        print ("Missing_Segment_File_start  = "+data2 + "\n") 
         
           
    except:
        print "Exception"
    finally:
        if f is not None:
            f.close()
        if f2 is not None:
            f2.close()
        if client is not None:
            client.close()

    