#!/usr/bin/python2.7
import paramiko
from paramiko import SSHClient
import paramiko
from scp import SCPClient
import sys
import os
#deviceIp = "192.168.200.158"
deviceIp = "192.168.1.103"
deviceIPs = ["192.168.1.103","192.168.1.152"]
user = "root"
passwd = "verizon123"

# # # # # # # # 
#!/Users/huanhe9/anaconda/bin/python
#from paramiko import SSHClient
#import paramiko
#from scp import SCPClient

host = "192.168.1.103"
deviceIPs = ["192.168.1.103","192.168.202.152","192.168.203.152","192.168.204.152"]
#user = 'root'
#passwd = 'verizon123'

#for device in deviceIPs:
#
 #   client = None
  #  f = None
#    try:
 #       client = paramiko.SSHClient()
  #      client.load_system_host_keys()
 #       client.set_missing_host_key_policy(paramiko.WarningPolicy())
  #      #client.connect("192.168.1.19",username="henry", password="boot12")
  #      client.connect(device,username= user, password= passwd)
    
                
   #     f = open (device + "-report.txt", "a+")      
       
    #    print("#### Test1: Get DVR app version and client build ####")
#       f = open ("report1.txt", "a+")      
     #   f.write  ("#### Test1: Get DVR app version and client build #### \n")
        
        
      #  stdin, stdout, stderr=client.exec_command('cat /data/app/Version.json')
       # data2 = stdout.read()
      #  line = data2.split('\n')
       # for lin in line:
#           f = open ("report1.txt", "a+")
        #    f.write(lin + "\n")
         #   print (lin)
        
        #stdin, stdout, stderr=client.exec_command('cat /etc/version.json')
        #data3 = stdout.read()
        #line = data3.split('\n')
        #for lin in line:
#           f = open ("report1.txt", "a+")
         #   f.write(lin + "\n")
          #  print (lin)
        #print (line)
        
    
        
        
 #   except:
  #      print "Exception"
  #  finally:
  #      if f is not None:
  #          f.close()
  #      if client is not None:
  #          client.close()



########## 
##########

for device in deviceIPs:
    ssh = None
    scp = None
    try:
        
        filepath = '/hd/data/logs/oncueapp/dvr_client.log'
        localpath = '/Users/huanhe9/GitHub/testpythonhomework2/'+ device +"_dvr_client.log"
        print ("local="+localpath)
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
        ssh.connect(device, username=user, password=passwd)

# SCPCLient takes a paramiko transport as its only argument
        scp = SCPClient(ssh.get_transport())

#scp.put('test.txt', 'test2.txt')
        scp.get(filepath, local_path=localpath)

#        scp.close()
    except:
        print "Exception"
    finally:
        if ssh is not None:
            ssh.close()
        if scp is not None:
            scp.close()

