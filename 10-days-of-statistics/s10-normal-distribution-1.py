import math

mu, sigma = list(map(float, input().split()))
x1 = float(input())
y1, y2 = list(map(float, input().split()))

def n(x):
    return (1 + math.erf((x - mu) / sigma / math.sqrt(2))) / 2

print('{:.3f}'.format(n(x1)))
print('{:.3f}'.format(n(y2) - n(y1)))

