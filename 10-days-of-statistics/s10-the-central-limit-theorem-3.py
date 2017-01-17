import math

n, pop_mu, pop_sigma, p, z = [float(input()) for _ in range(5)]
mu, sigma = pop_mu, pop_sigma / math.sqrt(n)
l, h = mu - z * sigma, mu + z * sigma
print('{:.2f}'.format(l))
print('{:.2f}'.format(h))