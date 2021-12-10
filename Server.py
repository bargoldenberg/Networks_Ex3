# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
SERVER_ADRESS = ('0.0.0.0',8000)
serverSocket.bind(SERVER_ADRESS)
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # set HTML file as outputdata
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\n\n'.encode()) # send OK response
        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:

# Send response message for file not found
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        connectionSocket.send(response.encode()) # send 404 File Not Found error
# Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data