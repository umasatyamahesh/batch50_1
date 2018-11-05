import threading
import time
c=0
def fun1():
	global c
	for i in range(10):
		print threading.current_thread()
		c=c+1
		time.sleep(1)
	print c
t1=threading.Thread(target=fun1,name="thread1")
t2=threading.Thread(target=fun1,name="thread2")
t1.start()
#t1.join()   # required to make sure 1 thread completes and then next starts when 1 function is shared by multiple threads , c=c+1 can get
	# impacted if join is not used and print erroneous results"	
t1.join(5) # It will allow t2 to start after 5 secs of t1 has started
t2.start()