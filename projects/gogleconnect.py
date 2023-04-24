import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("successfully connected to the server")
except socket.error as err:
    print("you have failed to connect to the server %s" %(err))
#connecting to google
port=80
try:
    host_ip=socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()
#connecting to th server
s.connect((host_ip,port))
print("the sockect has successfully connected to google")