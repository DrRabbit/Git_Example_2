import multiprocessing
import pickle
import time



def create_df(c):

	array = [i for i in range(5000000)]
	d = {c: array}
	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format(c)
	t0 = time.time()
	with open(path, 'wb') as handle:
		pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
	t1 = time.time()
	print('{0} pickled in {1}'.format(c, t1-t0))


if __name__ == '__main__':

	t_start = time.time()

	create_df('alex')
	create_df('cathy')

	# Load data (deserialize)
	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format('alex')
	t0 = time.time()
	with open(path, 'rb') as handle:
		data = pickle.load(handle)
	t1 = time.time()
	print('{0} UNpickled in {1}'.format('alex', t1-t0))

	path = 'C:\\Users\\Alex\\PycharmProjects\\Git_Example_2\\{}.pickle'.format('cathy')
	t0 = time.time()
	with open(path, 'rb') as handle:
		data = pickle.load(handle)
	t1 = time.time()
	print('{0} UNpickled in {1} \n'.format('cathy', t1-t0))

	t_end = time.time()

	print('total time: {0}'.format(t_end-t_start))