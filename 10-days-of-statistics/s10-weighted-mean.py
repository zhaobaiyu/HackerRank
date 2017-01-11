n = int(input())
x = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
print('{:.1f}'.format(sum([a * b for a, b in zip(x, w)]) / sum(w)))
