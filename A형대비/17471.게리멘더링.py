def grouping(k):
    if B:
        possible(A, B)


def possible(a, b):
    pass


def vote():
    pass


N = int(input())
population = [0] * (N + 1)
i = 1

for j in list(map(int, input().split())):
    population[i] = j
    i += 1

adjL = [[] for _ in range(N+1)]

i = 1
for _ in range(N):
    temp_lst = list(map(int, input().split()))
    n = temp_lst[0]
    for j in range(1, n+1):
        adjL[i].append(temp_lst[j])
    i += 1

visited = [0]*(N + 1)

arr = [i for i in range(1, N + 1)]
A = [arr[0]]
B = []
grouping(1)
vote()