T = int(input())
for t in range(T):
    a, b = input().split()
    cnt = a.count(b)
    result = len(a) - cnt*len(b) + cnt
    print(f'#{t+1}', result)