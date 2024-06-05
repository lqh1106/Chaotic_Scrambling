from numpy import mod
import sys
from math import pi, cos, acos, sin


def logistic(x0, m, n):
	x = x0
	for i in range(m):
		x = 3.60 * x * (1 - x)
	scramble = [x]
	for i in range(n - 1):
		scramble.append(3.60 * scramble[-1] * (1 - scramble[-1]))
	return sort(scramble)


def circle(x0, m, n):
	x = x0
	for i in range(m):
		x = mod(x + 0.2 - 0.5 / (2 * pi) * sin(2 * pi * x), 1)
	scramble = [x]
	for i in range(n - 1):
		scramble.append(mod(scramble[-1] + 0.2 - 0.5 / (2 * pi) * sin(2 * pi * scramble[-1]), 1))
	return sort(scramble)


def chebyshev(x0, m, n):
	x = x0
	for i in range(m):
		x = cos(4 * acos(x))
	scramble = [x]
	for i in range(n - 1):
		scramble.append(cos(4 * acos(scramble[-1])))
	return sort(scramble)


def sort(scrambling):
	sortedlist = sorted(scrambling)
	disorganizedtable = []
	for i in scrambling:
		disorganizedtable.append(sortedlist.index(i))
	# print(disorganizedtable)
	return disorganizedtable


def decode(c, way, k):
	m_list = [0] * len(c)
	if way == 0:
		disorganizedtable = logistic(k, 1000, len(c))
	elif way == 1:
		disorganizedtable = circle(k, 1000, len(c))
	elif way == 2:
		disorganizedtable = chebyshev(k, 1000, len(c))
	else:
		print("invalid way")

	dedisorganizedtable = [0] * len(disorganizedtable)

	for i in range(0, len(disorganizedtable)):
		dedisorganizedtable[i] = disorganizedtable.index(i)

	for i in range(0, len(dedisorganizedtable)):
		m_list[dedisorganizedtable[i]] = c[i]
	m = ''.join(m_list)
	return m


def encode(m, way, k):
	c_list = [0] * len(m)
	if way == 0:
		disorganizedtable = logistic(k, 1000, len(m))
	elif way == 1:
		disorganizedtable = circle(k, 1000, len(m))
	elif way == 2:
		disorganizedtable = chebyshev(k, 1000, len(m))
	else:
		print("invalid way")
	for i in range(0, len(disorganizedtable)):
		c_list[disorganizedtable[i]] = m[i]
	c = ''.join(c_list)
	return c


if __name__ == "__main__":
	m = input("enter your message: ")
	k = float(input("enter your key"))
	way = int(input("choose your way:(0-2)"))
	c = encode(m, way, k)
	print('Here is your cipher text: ' + c)
	print(decode(c, way, k))
