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
ypoints1 = []
ypoints2 = []
ypoints3 = []
k = 10000
for n in range(50, 1000):
	xpoints.append(n)
	order_total1 = 0
	order_total2 = 0
	order_total3 = 0
	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		disorganized_table = scrambling.logistic(3.6, x0, 1000, n)
		order_total1 += test.test(disorganized_table)
	ypoints1.append(order_total1 / (k * n))

	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		disorganized_table = scrambling.circle(0.5, 0.2, x0, 1000, n)
		order_total2 += test.test(disorganized_table)
	ypoints2.append(order_total2 / (k * n))

	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		disorganized_table = scrambling.chebyshev(4, x0, 1000, n)
		order_total3 += test.test(disorganized_table)
	ypoints3.append(order_total3 / (k * n))
	print(n, end=' ')
plot.plot(xpoints, ypoints1, 'Logistic', ypoints2, 'Circle', ypoints3, 'Chebyshev', filename='order_ave-N',
          title='order_ave-N')
