import threading
import time
c=0
def incre():
	global c
	print threading.current_thread()
	c=c+1
	print c
for i in range(5):
	t=threading.Thread(target=incre,name="%s"%i)
	t.start()
	t.join()   # required to make sure 1 thread completes and then next starts when 1 function is shared by multiple threads , c=c+1 can get
	# impacted if join is not used and print erroneous results"