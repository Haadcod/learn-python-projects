import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("You have successully connetcted to the socket")
except socket.error as err:
    print("socket creation has failed with %s" %(err))
#default port for socket
port=80
try:
    host_ip=socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("Ther was an error resolving the host")
    sys.exit()
#connecting to the server
s.connect((host_ip,port))
print("The socket has been successfully connected to google on port ==%s"%(host_ip))