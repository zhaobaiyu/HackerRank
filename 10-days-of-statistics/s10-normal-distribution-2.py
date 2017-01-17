import math

mu, sigma = list(map(float, input().split()))
x1 = float(input())
x2 = float(input())

def n(x):
    return (1 + math.erf((x - mu) / sigma / math.sqrt(2))) / 2

print('{:.2f}'.format((1 - n(x1)) * 100))
print('{:.2f}'.format((1 - n(x2)) * 100))
print('{:.2f}'.format(n(x2) * 100))

