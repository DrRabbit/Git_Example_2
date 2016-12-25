import multiprocessing
import pickle
import time


def create_df(c, q):

	array = [i for i in range(5000000)]
	# print('array created')
	d = {c: array}

	# Store data (serialize)
	# lock.acquire()
	# global path
	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format(c)
	t0 = time.time()
	with open(path, 'wb') as handle:
		pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
	t1 = time.time()
	print('{0} pickled in {1}'.format(c, t1-t0))
	# lock.release()


if __name__ == '__main__':

	t_start = time.time()
	q = multiprocessing.Queue()

	nm = 'alex'
	p1 = multiprocessing.Process(target=create_df, args=(nm, q))
	nm = 'cathy'
	p2 = multiprocessing.Process(target=create_df, args=(nm, q))

	print('starting p1')
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	# print('starting p2')

	print('\nall processes complete \n')

	# Load data (deserialize)
	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format('alex')
	t0 = time.time()
	with open(path, 'rb') as handle2:
		data = pickle.load(handle2)
	t1 = time.time()
	print('{0} UNpickled in {1}'.format('alex', t1-t0))

	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format('cathy')
	t0 = time.time()
	with open(path, 'rb') as handle2:
		data = pickle.load(handle2)
	t1 = time.time()
	print('{0} UNpickled in {1} \n'.format('cathy', t1-t0))


	'''
	for d in data.iteritems():
		print d
	'''

	'''
	dy = {}
	counter = 0
	while q.empty() is False:
		counter += 1
		# t0 = time.time()
		dy.update(q.get())
		# t1 = time.time()
		# print('time to update {0}, : {1}'.format(counter, t1-t0))
		print('done')
	'''
	t_end = time.time()
	print('total time: {0}'.format(t_end-t_start))

