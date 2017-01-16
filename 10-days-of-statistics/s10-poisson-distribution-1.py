import math

lambda_ = float(input().strip())
k_ = float(input().strip())

print('{:.3f}'.format(lambda_ ** k_ * math.exp(-lambda_) / math.factorial(k_)))
