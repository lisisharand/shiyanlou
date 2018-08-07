#!/usr/bin/env python3
from multiprocessing import Pool
def f(i):
	print(i)
def main():
	pool = 	Pool(processes = 3)
	for i in range(110):
		pool.apply(f,(i,))#what apply
	pool.close()
	pool.join()
if __name__ =='__main__':
	main()
