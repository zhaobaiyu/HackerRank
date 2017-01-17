import math
m, n, mu, sigma = [float(input()) for _ in range(4)]
mu = n * mu
sigma *= math.sqrt(n)

print('{:.4f}'.format((1 + math.erf((m - mu) / sigma / math.sqrt(2))) / 2))
