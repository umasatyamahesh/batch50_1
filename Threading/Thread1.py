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
dir_restart()
runningio()