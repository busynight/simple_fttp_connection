# *******************************************************************
# This file illustrates how to send a file using an
# application-level protocol where the first 10 bytes
# of the message from client to server contain the file
# size and the rest contain the file data.
# *******************************************************************
import socket
import os
import sys
import cmds
# Command line checks 
if len(sys.argv) < 3:
	print "USAGE python " + sys.argv[0] + " <SERVER_MACHINE> <SERVER_PORT>"

# Server address
serverAddr = int(sys.argv[1])

# Server port
serverPort = int(sys.arv[2])

# Create a command TCP socket
commSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect both sockets to the server
commSock.connect((serverAddr, serverPort))

# The number of bytes sent
numSent = 0


# Keep sending until all is sent
while True:
	
	

        cmd  = raw_input("ftp> ")
        
        newCmd = FTP_COMMANDS(cmd)

        if  newCmd.CheckCommand:
            cmdSizeStr = str(len(cmd))
                        

            while len(cmdSizeStr) < 10:
                cmdSizeStr = "0" + cmdSizeStr


                fileData = dataSizeStr + cmdSizeStr	
                        
                numSent = 0
                while len(fileData) > numSent:
                    numSent += connSock.send(fileData[numSent:])

            newCmd.RunCommand(commSock)
        

	
# Close both sockets
commSock.close()
dataSock.close()
	


