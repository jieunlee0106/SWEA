T = int(input())

def paper(N):
    if N % 10 == 0:
        if N == 10:
            return 1
        elif N == 20:
            return 3
        else:
            return paper(N-10)+(2*paper(N-20))


for t in range(T):
    N = int(input())
    count = paper(N)
    print(f"#{t+1}", count)


