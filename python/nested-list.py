if __name__ == '__main__':
    stu = {}
    s = []
    tmp = None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append(score)
        if stu.get(score) == None:
            stu[score] = [name]
        else:
            stu[score].append(name)
    min_ = min(s)
    for i in s:
        if tmp == None and i != min_:
            tmp = i
        elif i != min_ and i < tmp:
            tmp = i
    list(map(print, sorted(stu[tmp])))
