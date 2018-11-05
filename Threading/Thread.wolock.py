import threading
import time
c=0
#lock=threading.Lock()
def incre():
	global c #, lock
	print threading.current_thread()
	#lock.acquire()
	#time.sleep(1)
	c=c+1
	time.sleep(1)
	print c
	#lock.release()
for i in range(10):
	t=threading.Thread(target=incre,name="thread{%s}"%i)
	t.start()
	