for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x:x[1])

    print(lst)