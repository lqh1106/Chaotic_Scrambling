import scrambling
import test

print("Logistic:", end='')
disorganized_table = scrambling.logistic(3.6, 0.5, 1000, 500)
test.test(disorganized_table)

print("Circle:", end='')
disorganized_table = scrambling.circle(0.5, 0.2, 0.5, 1000, 500)
test.test(disorganized_table)

print("Chebyshev:", end='')
disorganized_table = scrambling.chebyshev(4, 0.6, 1000, 500)
test.test(disorganized_table)
