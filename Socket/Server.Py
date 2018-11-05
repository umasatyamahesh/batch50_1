import socket
hostname="ale143mahi"
port=8889
#TCP/UDP IPV4 IPV6
s=socket.socket()
try:
	s.bind((hostname,port))
	s.listen(6)
	print "Waiting for Client request"
	#print s.accept()
	clientobj,client_info=s.accept()
	clientobj.send('Connection Established Successfully')
	client_data=int(clientobj.recv(1024))
	if client_data%2==0:
		resp="Even"
	else:
		resp="Odd"
	clientobj.send(resp)
except Exception as err:
	print err
finally:
	s.close()
