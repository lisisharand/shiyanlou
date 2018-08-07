#!/usr/bin/env python3
import time
from multiprocessing import Process,Value,Lock 
def func(val,locka):
	for i in range(50):
		time.sleep(0.01)
		with lock:
			val.value += 1
	#	val.value += 1
	#with lock = lock.acquire()
	#	     val.value += 1
	#	     lock.release()
if __name__ =="__main__":
	v = Value('i',0)#why
	lock = Lock()
	procs = [Process(target = func,args =(v,lock)) for i in range(10)]#target = son process args= ruple

	for p in procs:
		p.start()
	for p in procs:
		p.join()
	print(v.value)
