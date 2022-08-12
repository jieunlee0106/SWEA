T = int(input())

for t in range(T):
    s = list(input())
    n = len(s)
    ans = 1
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            ans = 0
            break


    print(f'#{t+1}', ans)