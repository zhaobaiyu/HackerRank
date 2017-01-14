def median(l, beg, end):  # end is not included
    sep = end - beg
    if sep % 2 == 0:
        return (l[beg + sep // 2 - 1] + l[beg + sep // 2]) / 2
    else:
        return l[beg + sep // 2]

if __name__ == '__main__':
    n = int(input())
    x = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    zip_list = list(zip(x,f))
    zip_list.sort()
    s = []
    for i, j in zip_list:
        for _ in range(j):
            s.append(i)
    len_s = len(s)
    if len_s % 2 == 0:
        print('{:.1f}'.format(median(s, len_s // 2, len_s) - median(s, 0, len_s // 2)))
    else:
        print('{:.1f}'.format(median(s, len_s // 2 + 1, len_s) - median(s, 0, len_s // 2)))
