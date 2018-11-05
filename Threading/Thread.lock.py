import threading
import time
c=0
lock=threading.Lock()
def incre():
	global c, lock
	print threading.current_thread()
	lock.acquire()
	time.sleep(1)
	c=c+1
	print c
	lock.release()
	#print c
for i in range(5):
	t=threading.Thread(target=incre,name="thread{%s}"%i)
	t.start()
	