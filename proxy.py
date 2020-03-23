import socket
from socket import *
import argparse 

def main():
	# serverName = 'hostname'
	# serverPort = 12000
	# serverSocket = socket(AF_INET, SOCK_DGRAM)
	# serverSocket.bind(('', serverPort))
	# # message = raw_input('Input lowercase sentence:')
	# # clientSocket.sendto(message.encode(), (serverName, serverPort))
	# # print(serverPost)

	parser = argparse.ArgumentParser()
	parser.add_argument('port_number', nargs='?', type=int, default=8080)
	args=parser.parse_args()

	# print('Port Number')
	# print(args.port_number)

	# get port number from command line
	port_number = args.port_number

	# open a socket connection on startup and listen for incoming requests

	# on getting a request from the browser, proxy should parse the HTTP request to determine the destination server

	# open a connection to destination server

	# send request

	# process reply and send to browser



if __name__ == "__main__":
    main()