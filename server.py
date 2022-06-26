import socket

address='192.168.43.20'     #address of server
port=9998              #port number
n=3                     #no of connection
data=[]

#socket of server
s= socket.socket()  #default socket.AF_INET, socket.SOCK_STREAM  for v6 and UDP socket.AF_INET6, socket.SOCK_DGRAM

print("Socket Created")

#to bind a address with port number
s.bind((address,port))

#for number of connections 
s.listen(n)
print("Waiting for connections")

while True:
    #to accept a connection
    c,addr=s.accept()          #gives client socket and address
    name= c.recv(1024).decode()
    print("Connected with ",addr,name)
    try:
        c.send(bytes("Welcome to Server "+name,'utf-8'))
    except:
        c.send(bytes("Error in sending data"))
        c.close()
    data.append([addr[1],name])
    print("Port number and name of clients")
    print(data)
    tout=1
    while tout!=0:
        tout=1
        print("waiting for client response") 
        message=c.recv(1024).decode()        
        print("Client: "+message)                
        if "last request" in message: 
            tout=0
            print("waiting for client response")
            message=c.recv(1024).decode()            
            print("Client: "+message)

        message=''
        message=input("Server message: ")
        c.send(bytes(message,'utf-8'))
                     
                   
    print("Connection timeout")
    print("------------")
    print("Waiting for clients.....")
    
c.close()
s.close()

