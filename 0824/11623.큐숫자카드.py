for t in range(1, int(input())+1):
    n = int(input())
    num = [i for i in range(1, n + 1)]
    front = -1
    rear = -1
    while front != rear - 1:
        front = (front + 2) % n
        rear = (rear + 1) % n
        num[rear] = num[front]
    result = num[rear]
    print(f'#{t}', result)