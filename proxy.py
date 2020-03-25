from socket import *
import sys
import argparse

def proxy(port_number):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(('', port_number))
	sock.listen(1)
	while True:
		# open a socket connection on startup and listen for incoming requests
		connection, client_address = sock.accept()
		print("Connected")
		try:
			while True:
				# on getting a request from the browser, proxy should parse the HTTP request to determine the destination server
				data = connection.recv(1024)
				if data:
					print("http request from browser\n", data)
					first_line = data.decode().split('\n')[0].split()
					# parse the data for the destination
					if first_line[0] == 'GET':
						print("valid GET request received")

						# make connection to destination server
						domain = first_line[1][1:]
						remote_host = (domain, 80)
						print("About to connect to ", domain)
						s = socket(AF_INET, SOCK_STREAM)
						s.connect(remote_host)

						# send request for page
						# TODO don't hard code this
						s.sendall("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n".encode())

						while True:
							# process reply
							receive = s.recv(1024)
							print(repr(receive))
							if receive:
								print("Sending page to browser")
								# send reply to browser
								connection.send(receive)
							else:
								break
					else:
						print('Error: not implemented')
						# TODO should I be breaking?
						break

		finally:
			connection.close()

def main():
	# get port number from command line
	parser = argparse.ArgumentParser()
	parser.add_argument('port_number', nargs='?', type=int, default=8080)
	args=parser.parse_args()

	proxy(args.port_number)

if __name__ == "__main__":
    main()