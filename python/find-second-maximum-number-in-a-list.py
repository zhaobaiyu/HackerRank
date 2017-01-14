if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    max_ = max(list1)
    tmp = None
    for i,v in enumerate(list1):
        if tmp == None and v != max_:
            tmp = v
        if v != max_ and v > tmp:
            tmp = v
    print(tmp)
