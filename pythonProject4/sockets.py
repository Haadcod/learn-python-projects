#import socket module
import socket
#hosts and ports
host=''
port=8080
#creating a socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#setting socket options
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#bind the port to the socket
c.bind(host,port)
#binding done , we now tell a compter to wait and listen to that port
c.listen(1)
#handling a server request
while 1:
    csock,caddr=c.accept()
    cfile=csock.makefile('rw',0)
# sending data to the client
    line=cfile.readline().strip()
    cfile.write('HTTP/1.0 200 OK \n\n')
cfile

