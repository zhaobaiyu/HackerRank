import math

if __name__ == '__main__':
    n = int(input())
    x = [int(i) for i in input().split()]
    mu = sum(x) / n
    sigma = 0.0
    for i in x:
        sigma += (i - mu) ** 2
    sigma = math.sqrt(sigma / n)
    print('{:.1f}'.format(sigma))
