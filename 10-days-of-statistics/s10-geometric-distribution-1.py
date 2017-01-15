p1, p2 = list(map(int, input().split()))
n = int(input())
p = p1 / p2
print('{:.3f}'.format((1 - p) ** (n - 1) * p))