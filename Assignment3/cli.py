# *******************************************************************
# This file illustrates how to send a file using an
# application-level protocol where the first 10 bytes
# of the message from client to server contain the file
# size and the rest contain the file data.
# *******************************************************************
import socket
import os
import sys

# Command line checks 
if len(sys.argv) < 3:
	print "USAGE python " + sys.argv[0] + " <SERVER_MACHINE> <SERVER_PORT>" 

# Server address
serverAddr = sys.argv[1]

# Server port
serverPort = sys.arv[2]

# Create a command TCP socket
commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect both sockets to the server
commSock.connect((serverAddr, serverPort))

# The number of bytes sent
numSent = 0

#Check to see if the file is a valid command
def checkCMD(command):

        #Get the first argument of the command
        cmd_args = command.split(None, 1)

        #Compare with the list of given commands
        if cmd_args[0] != "ls" || cmd_args[0] != "get" || cmd_args[0] != "cd" || \
           cmd_args[0] != "mkdir" || cmd_args[0] != "quit" || cmd_args[0] != "remove" || \
           cmd_args[0] != "put" || cmd_args[0] != "remove":
                return False
        else:
                return True    

# Keep sending until all is sent
while True:
	
	

        cmd  = raw_input("ftp> ")
        
	if checkCMD(cmd):
                
		# Get the size of the data read
		# and convert it to string
		dataSizeStr = str(len(cmd))
		
		# Prepend 0's to the size string
		# until the size is 10 bytes
		while len(dataSizeStr) < 10:
			dataSizeStr = "0" + dataSizeStr
	
	
		# Prepend the size of the data to the
		# file data.
		fileData = dataSizeStr + fileData	
		
		# The number of bytes sent
		numSent = 0
		
		# Send the data!
		while len(fileData) > numSent:
			numSent += commSock.send(fileData[numSent:])
	
	# The file has been read. We are done
	else:
		break


print "Sent ", numSent, " bytes."
	
# Close both sockets
commSock.close()
dataSock.close()
	


