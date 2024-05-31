import math


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def lcm_of_list(numbers):
	lcm_result = numbers[0]
	for i in range(1, len(numbers)):
		lcm_result = (lcm_result * numbers[i]) // gcd(lcm_result, numbers[i])
	return lcm_result


def test(disorganized_table):
	order = []
	for i in disorganized_table:
		if i != -1:
			list = [disorganized_table.index(i)]
			disorganized_table[disorganized_table.index(i)] = -1
			j = i
			while j not in list:
				list.append(j)
				j = disorganized_table[j]
				disorganized_table[disorganized_table.index(j)] = -1
			disorganized_table[int(list[-1])] = -1
			order.append(len(list))
	Order = lcm_of_list(order)
	return Order
