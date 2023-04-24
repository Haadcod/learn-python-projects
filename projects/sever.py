#simple server-client program
import socket
#create the socket object
s=socket.socket()
print("Socket has been successfully created")
#Reserve a port in our computer in our case it can be 12345 buh it can also be something else
port=12345
#we bind to the port, we have not typed any ip field buh instead we have out an empty string which makes the server listen to requests coming from other computers on a network
s.bind(("",port))
print("Socket binded %s" %(port))
#Put the socket in listening mood
s.listen(5)
print("socket is listening")
#forever loop untill we interrupt it or an error occurs
while True:
    #Establish a connection with client
    c,addr=s.accept()
    print("Got connection from",addr)
    #Send a thank you message to the clirnt
    c.send("Thank you for connecting".encode())
    #close connection with the client
    c.close()
    #breaking once connection closed
    break
