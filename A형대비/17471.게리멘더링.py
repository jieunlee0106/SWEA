import copy
def grouping(k):
    global A_visited

    if A != [] and A not in A_visited:
        A_visited += [A.copy()]
        B = list(set(lst) - set(A))
        if B:
            possible(A, B)
    if k >= len(lst):
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
del_lst = []
for nn in range(1, N+1):
    temp_lst = list(map(int, input().split()))
    n = temp_lst[0]
    if n == 0:
        del_lst += [nn]
    else:
        for j in range(1, n+1):
            adjL[i].append(temp_lst[j])
    i += 1

lst = [x for x in lst if x not in del_lst]

if len(lst) == 0:
    print(-1)
else:
    A_visited = []
    A = [lst[0]]
    B = []
    ret = []
    ret_a = []
    ret_b = []
    grouping(1)
    mini = 1000000
    if len(ret):
        vote(ret)
        print(mini)
    else:
        print(-1)