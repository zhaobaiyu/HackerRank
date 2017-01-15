import math

temp1, temp2 = list(map(float, input().split()))
boy_p = temp1 / (temp1 + temp2)
n = 6
def cal(n, x, p):
    comb = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return comb * p ** x * (1 - p) ** (n - x)
sum = 0
for i in range(3, 7):
    sum += cal(n, i, boy_p)
print('{:.3f}'.format(sum))