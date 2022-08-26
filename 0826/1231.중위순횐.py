for t in range(10):
    n=  int(input())
    L = [0]*(n+1)
    R = [0]*(n+1)
    ch = [0]*(n+1) #알파벳 저장

    for _ in range(n):
        arr = input().split()
        num = int(arr[0])
        ch[num] = arr[1]

        if len(arr) == 4:
            L[num] = int(arr[2])
            R[num] = int(arr[3])
        elif len(arr) == 3:
            L[num] = int(arr[2])
    def inorder(v):
        if v == 0:
            return
        inorder(L[v])
        print(ch[v], end = '')
        inorder(R[v])

    print(f'#{t+1}', end=' ')
    inorder(1)
    print()




