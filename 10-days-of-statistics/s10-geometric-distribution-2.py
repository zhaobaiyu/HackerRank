p1, p2 = list(map(int, input().split()))
n = int(input())
p = p1 / p2
sum = 0
for i in range(5):
    sum += (1 - p) ** i * p
print('{:.3f}'.format(sum))