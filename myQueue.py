import multiprocessing as mp
import time


def myprint(d):
	for key, value in d.iteritems():
		print(key, value)
	print('\n')


def create_df(c, q):

	t0 = time.time()
	# 32768

	r = sum([i for i in xrange(1000000)])
	t1 = time.time()
	print(t1-t0)
	d = {c: r}
	q.put(d)


if __name__ == '__main__':
	q = mp.Queue()

	nm = 'alex'
	p1 = mp.Process(target=create_df, args=(nm, q))

	print('starting p1')
	p1.start()
	p1.join()

	dy = {}
	counter = 0

	while q.empty() is False:
		dy.update(q.get())
		myprint(dy)


	print('finished !')
