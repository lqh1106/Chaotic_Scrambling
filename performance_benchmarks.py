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
		time_list1 = []
		time_list2 = []
		time_list3 = []
		order_list1 = []
		order_list2 = []
		order_list3 = []
		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.logistic(x0, 1000, n)
			end_time = time.time()
			time_list1.append(end_time - start_time)
			order_list1.append(order_calculator.test(disorganized_table))
		ypoints1.append(np.mean(order_list1))
		tpoints1.append(np.mean(time_list1))

		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.circle(x0, 1000, n)
			end_time = time.time()
			time_list2.append(end_time - start_time)
			order_list2.append(order_calculator.test(disorganized_table))
		ypoints2.append(np.mean(order_list2))
		tpoints2.append(np.mean(time_list2))

		for i in range(test_count):
			x0 = random.uniform(0.2, 0.8)
			start_time = time.time()
			disorganized_table = scrambling.chebyshev(x0, 1000, n)
			end_time = time.time()
			time_list3.append(end_time - start_time)
			order_list3.append(order_calculator.test(disorganized_table))
		ypoints3.append(np.mean(order_list3))
		tpoints3.append(np.mean(time_list3))

		print(f'test time and order:N={n}')
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
		delta_list = []
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.logistic(x0, 1000, n)
				disorganized_table_delta = scrambling.logistic(x0 + delta, 1000, n)
				if np.array_equal(disorganized_table_origin, disorganized_table_delta):
					break
				delta = delta / 2
			delta_list.append(delta)
		spoints1.append(np.mean(delta_list))

		delta_list = []
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.circle(x0, 1000, n)
				disorganized_table_delta = scrambling.circle(x0 + delta, 1000, n)

				if np.array_equal(disorganized_table_origin, disorganized_table_delta):
					break
				delta = delta / 2
			delta_list.append(delta)
		spoints2.append(np.mean(delta_list))

		delta_list = []
		for j in range(test_count):
			delta = 0.25
			x0 = random.uniform(0.2, 0.75)
			for i in range(100):
				disorganized_table_origin = scrambling.chebyshev(x0, 1000, n)
				disorganized_table_delta = scrambling.chebyshev(x0 + delta, 1000, n)
				if np.array_equal(disorganized_table_origin, disorganized_table_delta):
					break
				delta = delta / 2
			delta_list.append(delta)
		spoints3.append(np.mean(delta_list))

		print(f'test sensitivity:N={n}')
	plot.plot(xpoints, spoints1, 'Logistic', spoints2, 'Circle', spoints3, 'Chebyshev', 'sensitivity_ave',
	          'sensitivity vs N',
	          'sensitivity vs N', test_count, test_range, True)


if __name__ == '__main__':
	test_count = 10000
	test_range = range(50, 1000)
	test_time_and_order(test_count, test_range)
	test_count = 1
	test_sensitivity(test_count, test_range)
