#!/Users/huanhe9/anaconda/bin/python

import paramiko
paramiko.util.log_to_file('/tmp/paramiko.log')
import os
import sys
import lib
import urllib
import lll

# Open a transport

host = "192.168.1.153"
port = 22
transport = paramiko.Transport((host, port))

# Auth

password = "verizon123"
username = "root"
transport.connect(username = username, password = password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download

filepath = '/hd/data/www/index.html'
localpath = '/Users/huanhe9/GitHub/testpythonhomework2'
sftp.get(filepath, localpath)

# Upload

#filepath = '/home/foo.jpg'
#localpath = '/home/pony.jpg'
#sftp.put(localpath, filepath)

# Close

sftp.close()
transport.close()
