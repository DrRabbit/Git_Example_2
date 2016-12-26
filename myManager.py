"""
I think the Manager updates "A-synchronous  ",
"""


from multiprocessing import Process, Manager
import multiprocessing as mp
import time
from os import getpid


def counter(d):
	# r = (i for i in range(1000000))
	r = [i for i in range(1000000)]
	d[mp.current_process().name] = r
	# d[getpid()] = r

if __name__ == '__main__':
	with Manager() as m:
		d = m.dict()

		processes = [Process(target=counter, args=(d, ), name=str(i)) for i in range(4)]

		for pro in processes:
			pro.start()

		for pro in processes:
			pro.join()

		for key in d.keys():
			print key, # d[key][-10:]

		x = 1
		print('finished')
