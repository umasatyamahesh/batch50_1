import socket
hostname=socket.gethostname()
port=8890
try:
	f=socket.socket()
	f.connect((hostname,port))
	ack=f.recv(1024)
	print 'response received from server %s'%ack
	f.send("12")
	resp=f.recv(1024)
	print 'respcode from server is %s'%resp
except Exception as err:
	print err
finally:
	f.close()