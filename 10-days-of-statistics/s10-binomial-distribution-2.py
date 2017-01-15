import math

p, n = list(map(float, input().split()))
p /= 100

def cal(n, x, p):
    comb = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return comb * p ** x * (1 - p) ** (n - x)

sum = 0
for i in range(3):
    sum += cal(n, i, p)
print('{:.3f}'.format(sum))
sum = 0
for i in range(2, int(n) + 1):
    sum += cal(n, i, p)
print('{:.3f}'.format(sum))
