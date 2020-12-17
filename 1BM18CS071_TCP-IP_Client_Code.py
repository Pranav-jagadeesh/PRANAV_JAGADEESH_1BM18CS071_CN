from socket import *
#serverName = '127.0.0.1'
serverName = 'DESKTOP-F25TF2L' # to find server name run folloeing two commands #import socket #socket.gethostname()
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter file name:")

clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print ('From Server:', filecontents)
clientSocket.close()
