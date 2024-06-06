import scrambling
import order_calculator
import time
import numpy as np
import random
import plot


def test_time_and_order(test_count, test_range):
	xpoints = []
	ypoints1 = []
	ypoints2 = []
	ypoints3 = []
	tpoints1 = []
	tpoints2 = []
	tpoints3 = []
	for n in test_range:
		xpoints.append(n)
		time_total1 = 0
		time_total2 = 0
		time_total3 = 0
		order_total1 = 0
		order_total2 = 0
		order_total3 = 0
		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.logistic(x0, 1000, n)
			end_time = time.time()
			time_total1 += (end_time - start_time)
			order_total1 += order_calculator.test(disorganized_table)
		ypoints1.append(order_total1 / test_count)
		tpoints1.append(time_total1 / test_count)

		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.circle(x0, 1000, n)
			end_time = time.time()
			time_total2 += (end_time - start_time)
			order_total2 += order_calculator.test(disorganized_table)
		ypoints2.append(order_total2 / test_count)
		tpoints2.append(time_total2 / test_count)

		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.chebyshev(x0, 1000, n)
			end_time = time.time()
			time_total3 += (end_time - start_time)
			order_total3 += order_calculator.test(disorganized_table)
		ypoints3.append(order_total3 / test_count)
		tpoints3.append(time_total3 / test_count)

		print(n, end=' ')
	plot.plot(xpoints, ypoints1, 'Logistic', ypoints2, 'Circle', ypoints3, 'Chebyshev', 'order_ave', 'order_ave vs N',
	          'order_ave vs N', test_count, test_range, True)
	plot.plot(xpoints, tpoints1, 'Logistic', tpoints2, 'Circle', tpoints3, 'Chebyshev', 'time_ave', 'time_ave vs N',
	          'time_ave vs N', test_count, test_range, False)


def test_sensitivity(test_count, test_range):
	xpoints = []
	spoints1 = []
	spoints2 = []
	spoints3 = []

	for n in test_range:
		xpoints.append(n)
		total_delta = 0
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.logistic(x0, 1000, n)
				disorganized_table_delta = scrambling.logistic(x0 + delta, 1000, n)
				if disorganized_table_origin == disorganized_table_delta:
					break
				delta = delta / 2
			total_delta += delta
		spoints1.append(total_delta / test_count)

		total_delta = 0
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.circle(x0, 1000, n)
				disorganized_table_delta = scrambling.circle(x0 + delta, 1000, n)
				if disorganized_table_origin == disorganized_table_delta:
					break
				delta = delta / 2
			total_delta += delta
		spoints2.append(total_delta / test_count)

		total_delta = 0
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.chebyshev(x0, 1000, n)
				disorganized_table_delta = scrambling.chebyshev(x0 + delta, 1000, n)
				if disorganized_table_origin == disorganized_table_delta:
					break
				delta = delta / 2
			total_delta += delta
		spoints3.append(total_delta / test_count)

		print(n, end=' ')
	plot.plot(xpoints, spoints1, 'Logistic', spoints2, 'Circle', spoints3, 'Chebyshev', 'sensitivity_ave', 'sensitivity vs N',
	          'sensitivity vs N', test_count, test_range, True)


if __name__ == '__main__':
	test_count = 1000
	test_range = range(50, 100)
	test_time_and_order(test_count, test_range)
	test_sensitivity(test_count, test_range)
