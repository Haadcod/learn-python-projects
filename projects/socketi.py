import socket
import sys
from Tools.scripts.fixcid import err

ip=socket.gethostbyname('www.google.com')
print(ip)
#example of a script connecting to google
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully created")
except:
    print("Socket creation failed with error %s" %(err))
#default port for sockect
port=80
try:
    host_ip=socket.gethostbyname('www.google.com')
except socket.gaierror:
    #This means couldnot resolve the host
    print("There was an Error resolving the host")
    sys.exit()
#connecting to the server
s.connect((host_ip,port))
print("You have successfully connected to the  ")