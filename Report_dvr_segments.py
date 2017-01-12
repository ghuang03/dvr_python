#!/usr/bin/python2.7
#import paramiko
import sys
import os
deviceIp = "192.168.1.101"
deviceIPs = ["192.168.1.101"]
# deviceIPs = ["192.168.1.103","192.168.202.152","192.168.203.152","192.168.204.152"]
user = "root"
passwd = "verizon123"

f = None
try:
    f = open('segment_info.txt')
#data2 = stdout.read()
 #   line = data2.split('\n')
    segment_data_dic = {}

    for line in f:

        key,value = line.split('=')
        key=key.strip()
        value=value.strip()
        value=value.rstrip('\n')

        if key in segment_data_dic:

            segment_data_dic.update({key:value })

        else:

            segment_data_dic[key] = [value]
    print segment_data_dic
except:
        print "Exception"
finally:
        if f is not None:
            f.close()
            
            
f = None
try:
    f = open('segment_data.txt')
#data2 = stdout.read()
 #   line = data2.split('\n')
    segment_data_dic = {}

    for line in f:

        key,value = line.split('=')
        key=key.strip()
        value=value.strip()
        value=value.rstrip('\n')

        if key in segment_data_dic:

            segment_data_dic.update({key:value })

        else:

            segment_data_dic[key] = [value]
    print segment_data_dic
except:
        print "Exception"
finally:
        if f is not None:
            f.close()        
#key:int(value) for key, value in segment_data_dic.iteritems()
#segment_data_dic_int = segment_data_dic((key, int(value)) for key, value in segment_data_dic.iteritems())
#segment_data_dic =[int(i) for i in segment_data_dic]

f = None
try:    
    f = open (deviceIp + "-report1.txt", "a+")      
    print("#### Test: Add segment increasement numbers for all channels  ####")    
    f.write("#### Test: Add segment increasement numbers for all channels  #### \n")
        

    print segment_data_dic
#print (segment_data_dic[KMTPDT_1MBm.m4v_start ])
    print (segment_data_dic.keys())
    print (segment_data_dic.values())
#new_dic = segment_data_dic()
    print ("                                                                          ")
    print ("# # # Calculate KGODT segments incremental during this test period # # # ")
    
#print (segment_data_dic['KMTPDT_5e192.m4a_start'])
#print (segment_data_dic['KMTPDT_5e192.m4a_end'])
#print (map(int,segment_data_dic['KMTPDT_5e192.m4a_end']))
#print (map(int,segment_data_dic['KMTPDT_5e192.m4a_start']))
    print ('KGODT_5e192.m4a segment:'); print (map(int,segment_data_dic['KGODT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KGODT_5e192.m4a_start'])[0])
#    segment = map(int,segment_data_dic['KGODT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KGODT_5e192.m4a_start'])[0]
#    print (segment)
    print ('KGODT_2e96.m4a segment:'); print (map(int,segment_data_dic['KGODT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KGODT_2e96.m4a_start'])[0])   
    print ('KGODT_01MBt.m4v segment:'); print (map(int,segment_data_dic['KGODT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KGODT_01MBt.m4v_start'])[0])
    print ('KGODT_1MBm.m4v segment:'); print (map(int,segment_data_dic['KGODT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KGODT_1MBm.m4v_start'])[0])
    print ('KGODT_5MBm.m4v segment:'); print (map(int,segment_data_dic['KGODT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KGODT_5MBm.m4v_start'])[0])
    
    f.write ("                                                                          \n")
    f.write ("# # # Calculate KGODT segments incremental during this test period # # # \n")
    f.write('KGODT_5e192.m4a segment increase:'); f.write(`map(int,segment_data_dic['KGODT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KGODT_5e192.m4a_start'])[0]`+'\n')
    f.write('KGODT_2e96.m4a segment increase:'); f.write(`map(int,segment_data_dic['KGODT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KGODT_2e96.m4a_start'])[0]`+'\n')
    f.write ('KGODT_01MBt.m4v segment increase:'); f.write (`map(int,segment_data_dic['KGODT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KGODT_01MBt.m4v_start'])[0]`+'\n')
    f.write ('KGODT_1MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KGODT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KGODT_1MBm.m4v_start'])[0]`+'\n')
    f.write ('KGODT_5MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KGODT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KGODT_5MBm.m4v_start'])[0]`+'\n')
    
    
    
    print ("                                                                          ")
    print ("# # # Calculate KPIXDT segments incremental during this test period # # # ")
    print ('KPIXDT_5e192.m4a segment:'); print (map(int,segment_data_dic['KPIXDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KPIXDT_5e192.m4a_start'])[0])
    print ('KPIXDT_2e96.m4a segment:'); print (map(int,segment_data_dic['KPIXDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KPIXDT_2e96.m4a_start'])[0])
    print ('KPIXDT_01MBt.m4v segment:'); print (map(int,segment_data_dic['KPIXDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_01MBt.m4v_start'])[0])
    print ('KPIXDT_1MBm.m4v segment:'); print (map(int,segment_data_dic['KPIXDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_1MBm.m4v_start'])[0])
    print ('KPIXDT_5MBm.m4v segment:'); print (map(int,segment_data_dic['KPIXDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_5MBm.m4v_start'])[0])
    
    f.write ("                                                                          \n")
    f.write ("# # # Calculate KPIXDT segments incremental during this test period # # #  \n")
    f.write ('KPIXDT_5e192.m4a segment increase:'); f.write (`map(int,segment_data_dic['KPIXDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KPIXDT_5e192.m4a_start'])[0]`+'\n')
    f.write ('KPIXDT_2e96.m4a segment increase:'); f.write (`map(int,segment_data_dic['KPIXDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KPIXDT_2e96.m4a_start'])[0]`+'\n')
    f.write ('KPIXDT_01MBt.m4v segment increase:'); f.write (`map(int,segment_data_dic['KPIXDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_01MBt.m4v_start'])[0]`+'\n')
    f.write ('KPIXDT_1MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KPIXDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_1MBm.m4v_start'])[0]`+'\n')
    f.write ('KPIXDT_5MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KPIXDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KPIXDT_5MBm.m4v_start'])[0]`+'\n')

    print ("                                                                          ")
    print ("# # # Calculate KTVUDT segments incremental during this test period # # # ")
    print ('KTVUDT_5e192.m4a segment:'); print (map(int,segment_data_dic['KTVUDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KTVUDT_5e192.m4a_start'])[0])
    print ('KTVUDT_2e96.m4a segment:');  print (map(int,segment_data_dic['KTVUDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KTVUDT_2e96.m4a_start'])[0])
    print ('KTVUDT_01MBt.m4v segment:'); print (map(int,segment_data_dic['KTVUDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_01MBt.m4v_start'])[0])
    print ('KTVUDT_1MBm.m4v segment:');  print (map(int,segment_data_dic['KTVUDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_1MBm.m4v_start'])[0])
    print ('KTVUDT_5MBm.m4v segment:');  print (map(int,segment_data_dic['KTVUDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_5MBm.m4v_start'])[0])

    f.write ("                                                                          \n")
    f.write ("# # # Calculate KTVUDT segments incremental during this test period # # # \n")
    f.write ('KTVUDT_5e192.m4a segment increase:'); f.write (`map(int,segment_data_dic['KTVUDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KTVUDT_5e192.m4a_start'])[0]`+'\n')
    f.write ('KTVUDT_2e96.m4a segment increase:');  f.write (`map(int,segment_data_dic['KTVUDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KTVUDT_2e96.m4a_start'])[0]`+'\n')
    f.write ('KTVUDT_01MBt.m4v segment increase:'); f.write (`map(int,segment_data_dic['KTVUDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_01MBt.m4v_start'])[0]`+'\n')
    f.write ('KTVUDT_1MBm.m4v segment increase:');  f.write (`map(int,segment_data_dic['KTVUDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_1MBm.m4v_start'])[0]`+'\n')
    f.write ('KTVUDT_5MBm.m4v segment increase:');  f.write (`map(int,segment_data_dic['KTVUDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KTVUDT_5MBm.m4v_start'])[0]`+'\n')


    print ("                                                                          ")
    print ("# # # Calculate KMTPDT segments incremental during this test period # # # ")
    print ('KMTPDT_5e192.m4a segment:'); print (map(int,segment_data_dic['KMTPDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_5e192.m4a_start'])[0])
    print ('KMTPDT_2e96.m4a segment:'); print (map(int,segment_data_dic['KMTPDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_2e96.m4a_start'])[0])
    print ('KMTPDT_01MBt.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_01MBt.m4v_start'])[0])
    print ('KMTPDT_1MBm.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_1MBm.m4v_start'])[0])
    print ('KMTPDT_5MBm.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_5MBm.m4v_start'])[0])

    f.write ("                                                                          \n")
    f.write ("# # # Calculate KMTPDT segments incremental during this test period # # # \n")
    f.write ('KMTPDT_5e192.m4a segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_5e192.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_5e192.m4a_start'])[0]`+'\n')
    f.write('KMTPDT_2e96.m4a segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_2e96.m4a_start'])[0]`+'\n')
    f.write ('KMTPDT_01MBt.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_01MBt.m4v_start'])[0]`+'\n')
    f.write ('KMTPDT_1MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_1MBm.m4v_start'])[0]`+'\n')
    f.write ('KMTPDT_5MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_5MBm.m4v_start'])[0]`+'\n')

    print ("                                                                          ")
    print ("# # # Calculate Missing segments incremental during this test period # # # ")
    print ('Missing File segment:'); print (map(int,segment_data_dic['Missing_Segment_File_end'])[0] - map(int,segment_data_dic['Missing_Segment_File_start'])[0])
#    print ('KMTPDT_2e96.m4a segment:'); print (map(int,segment_data_dic['KMTPDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_2e96.m4a_start'])[0])
#    print ('KMTPDT_01MBt.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_01MBt.m4v_start'])[0])
#    print ('KMTPDT_1MBm.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_1MBm.m4v_start'])[0])
#    print ('KMTPDT_5MBm.m4v segment:'); print (map(int,segment_data_dic['KMTPDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_5MBm.m4v_start'])[0])

    f.write ("                                                                          \n")
    f.write ("# # # Calculate Missing segments incremental during this test period # # # \n")
    f.write ('Missing File segment increase:'); f.write (`map(int,segment_data_dic['Missing_Segment_File_end'])[0] - map(int,segment_data_dic['Missing_Segment_File_start'])[0]`+'\n')
#    f.write('KMTPDT_2e96.m4a segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_2e96.m4a_end'])[0] - map(int,segment_data_dic['KMTPDT_2e96.m4a_start'])[0]`+'\n')
#    f.write ('KMTPDT_01MBt.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_01MBt.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_01MBt.m4v_start'])[0]`+'\n')
#    f.write ('KMTPDT_1MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_1MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_1MBm.m4v_start'])[0]`+'\n')
#    f.write ('KMTPDT_5MBm.m4v segment increase:'); f.write (`map(int,segment_data_dic['KMTPDT_5MBm.m4v_end'])[0] - map(int,segment_data_dic['KMTPDT_5MBm.m4v_start'])[0]`+'\n')


except:
        print "Exception"
finally:
        if f is not None:
            f.close()  

#data_dict {}
#import imp
##imp.load_source (name, pathname[, file])
#KMTPDT_1MBm.m4v_start ': [' 18899'
#KMTPDT_1MBm.m4v_end ': [' 18918']
#def getVarFromFile(filename):
#    import imp
#    f = open (filename)
#    global data
#    data = imp.load_source('data', '', f)
#    f.close()
    
#getVarFromFile (192.168.1.103_segment_data.txt)
#print (data.KTVUDT_5MBm.m4v_start)    




#>>> string = "abc=123,xyz=456"
#>>> dict(x.split('=') for x in string.split(','))
#{'xyz': '456', 'abc': '123'}


#f = open (segment_data.txt "rU")
 #   stdin, stdout, stderr=client.exec_command('cat segment_data.txt')
#    data2 = stdout.read()
 #   line = data2.split('\n')
 #   for lin in line:
#        data_dict(lin.slit ('='))
#           f = open ("report1.txt", "a+")
 #           f.write(lin + "\n")
 #       print (data_dict)
#f.close()
# f = open (device + "-report1.txt", "a+")      
#        print("#### Test: Dvr_SOAK_test_end.py  ####")
 #       print("#### Test1: Get DVR app version and client build ####")
#       f = open ("report1.txt", "a+")      
#        f.write  ("#### Test1: Get DVR app version and client build #### \n")
        
        
#        stdin, stdout, stderr=client.exec_command('cat /data/app/Version.json')
#        data2 = stdout.read()
#        line = data2.split('\n')
#        for lin in line:
#           f = open ("report1.txt", "a+")
#            f.write(lin + "\n")
#            print (lin)
        



