import numpy as np
def lcm_of_list(lst):
    if len(lst) == 0:
        return 1
    lcm = lst[0]
    for i in range(1, len(lst)):
        lcm = np.lcm(lcm, lst[i])
    return lcm

def test(disorganized_table):
	visited = set()
	order = []

	for i, val in enumerate(disorganized_table):
		if val != -1 and i not in visited:
			cycle_length = 0
			j = i
			while j not in visited:
				visited.add(j)
				j = disorganized_table[j]
				cycle_length += 1
			order.append(cycle_length)

	return lcm_of_list(order) if order else 1
