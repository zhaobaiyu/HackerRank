import numpy as np
from scipy import stats
n = int(input())
list1 = [int(x) for x in input().split()]
print('{:.1f}'.format(np.mean(list1)))
print('{:.1f}'.format(np.median(list1)))
print(stats.mode(list1)[0][0])
