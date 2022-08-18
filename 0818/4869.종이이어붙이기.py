T = int(input())
for t in range(T):
    l = int(input())
    h = 20
    k = l//20
    m = l/10
    bg = 0
    stack = []
    p1, p1_1, p2 = [10, 20], [20, 10], [20, 20]
    if l % 20 == 0:
        bg = (3**k) + (3**(k-1))
    else:
        for i in range(1, m+1):
            for j in range()

