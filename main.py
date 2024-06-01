import scrambling
import test
import time
import numpy as np
import random
import plot
import concurrent.futures
import random
import time
import scrambling
import test


def generate_data(n):
	order1 = {}
	order2 = {}
	order3 = {}
	time1 = {}
	time2 = {}
	time3 = {}
	k = 10000

	for n_val in range(50, n):
		time_total1 = 0
		time_total2 = 0
		time_total3 = 0
		order_total1 = 0
		order_total2 = 0
		order_total3 = 0

		for i in range(k):
			x0 = random.uniform(0, 1)
			start_time = time.time()
			disorganized_table = scrambling.logistic(3.6, x0, 1000, n_val)
			end_time = time.time()
			time_total1 += (end_time - start_time)
			order_total1 += test.test(disorganized_table)

		order1[n_val] = (order_total1 / k)
		time1[n_val] = (time_total1 / k)

		for i in range(k):
			x0 = random.uniform(0, 1)
			start_time = time.time()
			disorganized_table = scrambling.logistic(3.6, x0, 1000, n_val)
			end_time = time.time()
			time_total2 += (end_time - start_time)
			order_total2 += test.test(disorganized_table)

		order2[n_val] = (order_total2 / k)
		time2[n_val] = (time_total2 / k)

		for i in range(k):
			x0 = random.uniform(0, 1)
			start_time = time.time()
			disorganized_table = scrambling.logistic(3.6, x0, 1000, n_val)
			end_time = time.time()
			time_total3 += (end_time - start_time)
			order_total3 += test.test(disorganized_table)

		order3[n_val] = (order_total3 / k)
		time3[n_val] = (time_total3 / k)

	return order1, order2, order3, time1, time2, time3


def main():
	n_values = range(50, 1000)  # 或者您想要的其他范围
	data_points = []

	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
		future_to_n = {executor.submit(generate_data, n): n for n in n_values}
		for future in concurrent.futures.as_completed(future_to_n):
			n = future_to_n[future]
			try:
				data_points.append(future.result())
				print(f"Finished processing n={n}")
			except Exception as exc:
				print(f"Error processing n={n}: {exc}")
	order1 = {}
	order2 = {}
	order3 = {}
	time1 = {}
	time2 = {}
	time3 = {}
	for data in data_points:
		order1 = {**order1, **data[0]}
		order2 = {**order2, **data[1]}
		order3 = {**order3, **data[2]}
		time1 = {**time1, **data[3]}
		time2 = {**time2, **data[4]}
		time3 = {**time3, **data[5]}
	sorted_keys = sorted(order1.keys())
	xpoints = sorted_keys
	ypoints1 = [order1[key] for key in sorted_keys]

	sorted_keys = sorted(order2.keys())
	ypoints2 = [order2[key] for key in sorted_keys]

	sorted_keys = sorted(order3.keys())
	ypoints3 = [order3[key] for key in sorted_keys]

	sorted_keys = sorted(time1.keys())
	tpoints1 = [time1[key] for key in sorted_keys]

	sorted_keys = sorted(time2.keys())
	tpoints2 = [time2[key] for key in sorted_keys]

	sorted_keys = sorted(time3.keys())
	tpoints3 = [time3[key] for key in sorted_keys]

	plot.plot(xpoints, ypoints1, 'Logistic', ypoints2, 'Circle', ypoints3, 'Chebyshev', 'order_ave',
	          filename='order_ave-N', title='order_ave-N')

	plot.plot(xpoints, tpoints1, 'Logistic', tpoints2, 'Circle', tpoints3, 'Chebyshev', 'time_ave',
	          filename='time_ave-N', title='time_ave-N')


if __name__ == "__main__":
	main()
