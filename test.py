import threading
import time


class MyThread(threading.Thread):
    def run(self):
    	n=0
    	for i in range (6000):
        	n=+1
    	#print("done")

start = time.time()
for i in range(10):
	t = MyThread()
	t.run()

t.join
print (time.time()-start)
start = time.time()
for i in range(10):
	n=0
	for j in range(6000):
		n=+1
	#print("done")		
print (time.time()-start)