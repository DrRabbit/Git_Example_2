
# import time
# import memory_profiler
import sys
from PyQt4 import QtGui, QtCore
import numpy as np

'''
print('before memory usage: {}'.format(memory_profiler.memory_usage()))
t0 = time.time()
gen = (i for i in range(10000000))

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
'''


def print_me():
	print('hello')

a = np.random.rand(5, 2)


app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(400, 300)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()

btn = QtGui.QPushButton('hello', w)
btn.connect(btn, QtCore.SIGNAL('clicked()'), print_me)
btn.show()

w.setStyleSheet("background-color: rgb(255, 130, 255);"
                "alternate-background-color: rgb(0, 170, 127);"
                "selection-background-color: rgb(148, 148, 148);")


sys.exit(app.exec_())


