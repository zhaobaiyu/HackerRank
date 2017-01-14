def median(l, beg, end):  # end is not included
    sep = end - beg
    if sep % 2 == 0:
        return (l[beg + sep // 2 - 1] + l[beg + sep // 2]) // 2
    else:
        return l[beg + sep // 2]

if __name__ == '__main__':
    n = int(input())
    x = [int(i) for i in input().split()]
    x.sort()
    len_x = len(x)
    if len_x % 2 == 0:
        print(median(x, 0, len_x // 2), median(x, 0, len_x), median(x, len_x // 2, len_x), sep='\n')
    else:
        print(median(x, 0, len_x // 2), median(x, 0, len_x), median(x, len_x // 2 + 1, len_x), sep='\n')
