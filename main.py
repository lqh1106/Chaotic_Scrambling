import scrambling
import test
import time
import numpy as np
import random
import plot

xpoints = []
ypoints1 = []
ypoints2 = []
ypoints3 = []
tpoints1 = []
tpoints2 = []
tpoints3 = []
k = 10000
for n in range(50, 100):
	xpoints.append(n)
	time_total1 = 0
	time_total2 = 0
	time_total3 = 0
	order_total1 = 0
	order_total2 = 0
	order_total3 = 0
	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		start_time = time.time()
		disorganized_table = scrambling.logistic(x0, 1000, n)
		end_time = time.time()
		time_total1 += (end_time - start_time)
		order_total1 += test.test(disorganized_table)
	ypoints1.append(order_total1 / (k * n))
	tpoints1.append(time_total1 / k)

	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		start_time = time.time()
		disorganized_table = scrambling.circle(x0, 1000, n)
		end_time = time.time()
		time_total2 += (end_time - start_time)
		order_total2 += test.test(disorganized_table)
	ypoints2.append(order_total2 / (k * n))
	tpoints2.append(time_total2 / k)

	for i in range(k):
		x0 = random.uniform(0.2, 0.8)
		start_time = time.time()
		disorganized_table = scrambling.chebyshev(x0, 1000, n)
		end_time = time.time()
		time_total3 += (end_time - start_time)
		order_total3 += test.test(disorganized_table)
	ypoints3.append(order_total3 / (k * n))
	tpoints3.append(time_total3 / k)

	print(n, end=' ')
plot.plot(xpoints, ypoints1, 'Logistic', ypoints2, 'Circle', ypoints3, 'Chebyshev', 'order_ave', filename='order_ave-N',
          title='order_ave-N')
plot.plot(xpoints, tpoints1, 'Logistic', tpoints2, 'Circle', tpoints3, 'Chebyshev', 'time_ave', filename='time_ave-N',
          title='time_ave-N')
