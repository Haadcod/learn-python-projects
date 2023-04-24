import socket
s=socket.socket()
print("The socke has been created succefully")
#Reserve a port on the computer
port=12345
#bind to the port
#we hav not typed any ip in the string field which makes it listen to all requests from differnt computers
s.bind(("",port))
print("socket binded to %s"%(port))
#socket into listening mode
s.listen(5)
print("Socket is in listening mode")
#for ever loop until we interrupt it or an error occurs
while True:
    #Establish a connection with a client
    c,addr=s.accept()
    print("Got connection from",addr)
    #send a thank you message to thr client
    c.send("Thank you for connecting ")
    c.close()