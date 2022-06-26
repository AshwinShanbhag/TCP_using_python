import socket

address='localhost'       # 172.16.3.108 address of server
port= 9998              #port number of server
tout=2
#socket for client
c=socket.socket()   #default socket.AF_INET, socket.SOCK_STREAM --> TCP

#address of server
try:
    c.connect((address,port))
    print("Connected to server")
except:
    print("Error in connection. Check IP address")
    exit()

name=input("Enter your name: ")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())

while tout!=0:
    message=''
    message=input("Client message: ")
    c.send(bytes(message,'utf-8'))
    print("waiting for server response")
    print("Server: " + c.recv(1024).decode())
    tout-=1
    if tout==1:
        message="NOTE: This is the last request to client"
        print(message)
        c.send(bytes("last request",'utf-8'))
    
c.close()




