#!/usr/bin/env python3
import threading
def hello(name):
	print('child thread: {}'.format(threading.get_ident()))
	print('HELLO' +name)
def main():
	t = threading.Thread(target = hello,args=('love',))
	t.start()
	t.join()
	print('main threading: {}'.format(threading.get_ident()))
if __name__ =='__main__':
	main()
