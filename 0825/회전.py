for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    Q = [0]*(n+1)
    front = 1
    rear = 1
    for i in range(1, n+1):
        Q[i] = nums[i-1]


    for j in range(m):
        Q[(rear-1)%(n+1)] = Q[rear]
        rear = (rear+1)%(n+1)
        front = (front+1)%(n+1)
    print(f'#{t}', Q[front])