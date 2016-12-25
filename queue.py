import multiprocessing
import sys
from random import random
import numpy as np
import time

lock = multiprocessing.Lock()

def myprint(d):
	for key, value in d.iteritems():
		print(key, value)


def create_df(c, q):
	lock.acquire()
	t0 = time.time()
	r = [i for i in xrange(10000)]
	t1 = time.time()
	print(t1-t0)


	d = {}
	d[c] = r
	q.put(d)
	lock.release()

	# t2 = time.time()
	# print('add {0} to Queue {1}'.format(c, t2-t1))


if __name__ == '__main__':
	q = multiprocessing.Queue()

	nm = 'alex'
	p1 = multiprocessing.Process(target=create_df, args=(nm, q))
	# name = 'cathy'
	# p2 = multiprocessing.Process(target=create_df, args=(name, q, ))

	print('starting p1')
	try:
		p1.start()
		p1.join()
	except:
		print('something went wrong')
		sys.exit()

	# p2.start()
	# p2.join()

	print('all processes complete')

	dy = {}
	counter = 0
	while q.empty() is False:
		counter += 1
		# t0 = time.time()
		dy.update(q.get())
		# t1 = time.time()
		# print('time to update {0}, : {1}'.format(counter, t1-t0))
		print('done')

	# myprint(d)



