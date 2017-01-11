if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(N):
        para = input().split()
        if para[0] == 'insert':
            ans.insert(int(para[1]), int(para[2]))
        elif para[0] == 'print':
            print(ans)
        elif para[0] == 'remove':
            ans.remove(int(para[1]))
        elif para[0] == 'append':
            ans.append(int(para[1]))
        elif para[0] == 'sort':
            ans.sort()
        elif para[0] == 'pop':
            ans.pop()
        elif para[0] == 'reverse':
            ans.reverse()
