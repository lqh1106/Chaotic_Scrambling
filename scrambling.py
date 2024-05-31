import numpy as np
import math


def logistic(u, x0, m, n):
	if 3.57 <= u <= 4:
		x = x0
		for i in range(m):
			x = u * x * (1 - x)
		scramble = [x]
		for i in range(n):
			scramble.append(u * scramble[-1] * (1 - scramble[-1]))
		return sort(scramble)
	else:
		print("Please choose u in range[3.57,4]")


def circle(a, b, x0, m, n):
	x = x0
	for i in range(m):
		x = np.mod(x + b - a / (2 * math.pi) * math.sin(2 * math.pi * x), 1)
	scramble = [x]
	for i in range(n):
		scramble.append(np.mod(scramble[-1] + b - a / (2 * math.pi) * math.sin(2 * math.pi * scramble[-1]), 1))
	return sort(scramble)


def chebyshev(a, x0, m, n):
	x = x0
	for i in range(m):
		x = math.cos(a * math.acos(x))
	scramble = [x]
	for i in range(n):
		scramble.append(math.cos(a * math.acos(scramble[-1])))
	return sort(scramble)



def sort(scrambling):
	sortedlist = sorted(scrambling)
	disorganizedtable = []
	for i in scrambling:
		disorganizedtable.append(sortedlist.index(i))
	# print(disorganizedtable)
	return disorganizedtable
