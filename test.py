import time
import memory_profiler


print('before memory usage: {}'.format(memory_profiler.memory_usage()))
t0 = time.time()
gen = [i for i in xrange(10000000)]
t1 = time.time()
print('create the gen {}'.format(t1-t0))

t2 = time.time()
mySum = 0
for g in gen:
	mySum += g
t3 = time.time()
print('loop through list {}'.format(t3 - t2))

print('sum = {}'.format(mySum))

print('total time {}'.format(t3-t0))
print('AFTER memory usage: {}'.format(memory_profiler.memory_usage()))


