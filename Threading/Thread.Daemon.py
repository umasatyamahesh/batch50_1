import threading
import time
def dir_restart():
	print threading.current_thread()
	for i in range(5):
		print "Directory Restart"
		time.sleep(1)
def runningio():
	print threading.current_thread()
	for i in range(5):
		print "runningio"
		time.sleep(1)
def check_status():
	print 'Checking Status'
dirt=threading.Thread(target=dir_restart,name="dirt")
io=threading.Thread(target=runningio,name="io")
dirt.setDaemon(True)
io.setDaemon(True)
dirt.start()
io.start()
print dirt.is_alive()
time.sleep(2)
check_status()
