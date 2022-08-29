for tc in range(1,int(input()) + 1):
    data = input()
    version = '0'
    cnt = 0
    for d in data:
        if d != version:
            version = d
            cnt += 1
    print(f'#{tc}', cnt)