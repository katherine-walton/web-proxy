from socket import *
import sys
import argparse

def proxy(port_number):
	proxy_socket = socket(AF_INET, SOCK_STREAM)
	proxy_socket.bind(('', port_number))
	proxy_socket.listen(1)
	while True:
		# open a socket connection on startup and listen for incoming requests
		connection, addr = proxy_socket.accept()
		print("Connected")
		# on getting a request from the browser, proxy should parse the HTTP request to determine the destination server
		data = connection.recv(1024)
		if data:
			print("http request from browser\n", data)
			first_line = data.decode().split('\n')[0].split()
			# parse the data for the destination
			if first_line[0] == 'GET':
				print("valid GET request received")

				# make connection to destination server
				split_address = first_line[1][1:].split('/', 1)
				domain = split_address[0]
				if len(split_address) > 1:
					url = split_address[1]
				else:
					url='/'
				
				print("About to connect to ", domain)
				s = socket(AF_INET, SOCK_STREAM)
				remote_host = (domain, 80)
				s.connect(remote_host)

				# send request for page
				request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n"
				s.sendall(request.format(url, domain).encode())

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
				break


def main():
	# get port number from command line
	parser = argparse.ArgumentParser()
	parser.add_argument('port_number', nargs='?', type=int, default=8080)
	args=parser.parse_args()

	proxy(args.port_number)

if __name__ == "__main__":
    main()