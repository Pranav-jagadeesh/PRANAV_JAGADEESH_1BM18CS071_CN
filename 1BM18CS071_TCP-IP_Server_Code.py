from socket import *
#serverName='127.0.0.1'
serverName = 'DESKTOP-F25TF2L'# to find server name run folloeing two commands #import socket #socket.gethostname()
serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    file=open(sentence,"r")
    l=file.read(1024)
    print (l)
    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
