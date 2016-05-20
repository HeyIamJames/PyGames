#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print "-" * 60
print "scanning remote host", remoteServerIP
print "-" * 60
