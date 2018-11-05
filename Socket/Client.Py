import socket
hostname="ale143mahi"
port=8889
#TCP/UDP IPV4 IPV6
f=socket.socket()
try:
	f.connect((hostname,port))
	ack=f.recv(1024)
	print "Response received from server: %s"%ack
	f.send("12")
	resp=f.recv(1024)
	print "resp is %s"%resp
except Exception as err:
	print err
finally:
	f.close()