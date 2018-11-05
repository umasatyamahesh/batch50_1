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
#dir_restart()
#runningio()
#dirt=threading.Thread(target=dir_restart,name="dirt")
dirt=threading.Timer(10,dir_restart)
io=threading.Thread(target=runningio,name="io")
dirt.start()
io.start()
print dirt.is_alive()
check_status()
#print threading.enumerate()
#print threading.active_count()