# *****************************************************
# This file implements a server for receiving the file
# sent using sendfile(). The server receives a file and
# prints it's contents.
# *****************************************************

import socket
import cmds
import sys
# The port on which to listen
listenPort = 1234


# Command line checks 
if len(sys.argv) < 3:
        print "USAGE python " + sys.argv[0] + " <SERVER_PORT>" 

# Create a welcome socket. 
welcomeSock = socket.socket(socket.AF_INET, int(socket.sys.argv[1]))


# Bind the socket to the port
welcomeSock.bind(('', listenPort))

# Start listening on the socket
welcomeSock.listen(1)


print welcomeSock.sockaddress()

# ************************************************
# Receives the specified number of bytes
# from the specified socket
# @param sock - the socket from which to receive
# @param numBytes - the number of bytes to receive
# @return - the bytes received
# *************************************************
def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff
		
# Accept connections forever
while True:
	
	print "Waiting for connections..."
		
	# Accept connections
	clientSock, addr = welcomeSock.accept()
	
	print "Accepted connection from client: ", addr
	print "\n"
	
	fileData = ""
	
	# The temporary buffer to store the received
	# data.
	recvBuff = ""
	
	# The size of the incoming command
	cmdSize = 0	
	
	# The buffer containing the file size
	cmdSizeBuff = ""
	
	# Receive the first 10 bytes indicating the
	# size of the command
	cmdSizeBuff = recvAll(clientSock, 10)
		
	# Get the command size
	cmdSize = int(fileSizeBuff)


	
	print "The Command size is ", fileSize
	
	# Get the command data
	cmdData = recvAll(clientSock, fileSize)
	
	print "The command is: "
	print cmdData

	serverCmd = FTP_COMMANDS (cmdData)

	serverCmd.RunCommand(welcomeSock)
		
	# Close our side
	clientSock.close()
	
