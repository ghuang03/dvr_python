#!/Users/huanhe9/anaconda/bin/python
from paramiko import SSHClient
import paramiko
from scp import SCPClient
import os

host = "192.168.1.153"
user = 'root'
passwd = 'verizon123'

filepath = '/hd/data/www/index.html'
localpath = '/Users/huanhe9/GitHub/testpythonhomework2/'+ host +"dvr_client.log"
print ("locl="+localpath)
print ("Hello")
print ("master")
print ("feature1")
print ("add script")

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.connect(host, username=user, password=passwd)

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

#scp.put('test.txt', 'test2.txt')
scp.get(filepath, local_path=localpath)

scp.close()

