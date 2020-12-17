from socket import *
#serverName = '127.0.0.1'
serverName = 'DESKTOP-F25TF2L'# to find server name run folloeing two commands #import socket #socket.gethostname()
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input("Enter file name:")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName, serverPort))
filecontents,serverAddress = clientSocket.recvfrom(2048)
print ('From Server:', filecontents.decode())
clientSocket.close()