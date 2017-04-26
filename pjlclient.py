'''
PJL Client
Author: Hacktive Security - Carlo <wrynux> Pelliccioni
'''

import socket
import sys
import time

def conn(string,host):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 9100))
        s.send(string)
        time.sleep(5)
        print s.recv(30720)
    except:
            print 'Socket error'
            pass
     
def cmdlist(cmd,host,path):
    if sys.argv[2] == 'dir':
        cmd = '\x1b%-12345X@PJL FSDIRLIST NAME="0:' + path + '" ENTRY=1 COUNT=999999\x0d\x0a\x1b%-12345X\x0d\x0a'
        conn(cmd,host)
    elif sys.argv[2] == 'read':
        try:
            cmd = '\x1b%-12345X@PJL FSUPLOAD NAME="0:'+ path +'" OFFSET=0 SIZE=999999\x0d\x0a\x1b%-12345X\x0d\x0a'
            conn(cmd,host)
        except:
            print 'Select an existent path'
            pass
    else:
        print 'Usage: <IP> <dir|read> <path>'

cmdlist(sys.argv[2],sys.argv[1],sys.argv[3])
