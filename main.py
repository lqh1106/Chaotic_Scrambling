import scrambling
import test
import time
import numpy as np
import random
import plot

# print("Logistic:", end='')
# start_time = time.time()
# disorganized_table = scrambling.logistic(3.6, 0.5, 1000, 500)
# end_time = time.time()
# test.test(disorganized_table)
# print("Time taken:", end_time - start_time)
#
# print("Circle:", end='')
# start_time = time.time()
# disorganized_table = scrambling.circle(0.5, 0.2, 0.5, 1000, 500)
# end_time = time.time()
# test.test(disorganized_table)
# print("Time taken:", end_time - start_time)
#
# print("Chebyshev:", end='')
# start_time = time.time()
# disorganized_table = scrambling.chebyshev(4, 0.6, 1000, 500)
# end_time = time.time()
# test.test(disorganized_table)
# print("Time taken:", end_time - start_time)
xpoints = []
ypoints = []
for n in range(50, 1000):
	xpoints.append(n)
	order_total = 0
	x0_min = 0.2
	x0_max = 0.8
	for i in range(100):
		x0 = random.uniform(x0_min, x0_max)
		disorganized_table = scrambling.logistic(3.6, x0, 1000, n)
		order_total += test.test(disorganized_table)
	ypoints.append(order_total / ((i + 1)))
plot.plot(xpoints, ypoints, 'Logistic', "x0 in (" + str(x0_min) + ',' + str(x0_max) + ')')
