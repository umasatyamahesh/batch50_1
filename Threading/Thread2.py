import threading
import time
def dir_restart():
	for i in range(5):
		print "Directory Restart"
		time.sleep(1)
def runningio():
	for i in range(5):
		print "runningio"
		time.sleep(1)
#dir_restart()
#runningio()
dirt=threading.Thread(target=dir_restart)
io=threading.Thread(target=runningio)
dirt.start()
io.start()