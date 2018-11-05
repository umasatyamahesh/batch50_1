import socket
hostname=socket.gethostname()
print hostname
port=8890
try:
	s=socket.socket()
	s.bind((hostname,port))
	s.listen(10)
	cli_obj,cli_info=s.accept()
	cli_obj.send("Connection Successful!!!")
	data=int(cli_obj.recv(1024))
	cli_obj.send("Even" if (data%2)==0 else "odd")
except Exception as err:
	print err
except:
	s.close()
finally:
	s.close()
