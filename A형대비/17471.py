import copy
from collections import deque
def grouping(k):
    global A_visited

    if A != [] and A not in A_visited:
        B = list(set(lst) - set(A))
        A_visited += [B.copy()]
        if B and A:
            print('A =>', A, 'B=>', B)
            possible(A, B)
    if k >= N:
        return
    A.append(lst[k])
    grouping(k + 1)
    A.pop()
    grouping(k + 1)

def possible(A, B):
    global ret
    V = []
    for a in A:
        for aa in adjL[a]:
            if aa in A:
                V += [aa]
    V = set(V)
    V = list(V)
    if sorted(A) != sorted(V):
        return
    else:
        V = []
        for b in B:
            for bb in adjL[b]:
                if bb in B:
                    V += [bb]

        V = set(V)
        V = list(V)
        if sorted(B) != sorted(V):
            return

        else:
            a_lst = A.copy()
            b_lst = B.copy()
            ret += [[a_lst, b_lst]]


def vote(ret):
    global mini, ret_a, ret_b
    while ret:
        a_lst, b_lst = ret.pop()
        a_vote, b_vote = 0, 0
        for a in a_lst:
            a_vote += population[a]
        for b in b_lst:
            b_vote += population[b]

        if abs(a_vote - b_vote) < mini:
            mini = abs(a_vote - b_vote)
            ret_a = a_lst
            ret_b = b_lst


N = int(input())
population = [0] * (N + 1)
lst = [i for i in range(1, N + 1)]

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

A_visited = []
A = []
B = []
ret = []
ret_a = []
ret_b = []
grouping(0)
mini = 1000000
if len(ret):
    vote(ret)
    print('ret_a', ret_a, 'ret_b', ret_b)
    print(mini)
else:
    print(-1)