import copy
lst = [1, 2, 3, 4, 5, 6]
a =[lst[0]]
alst = []
def ba(k):
    global alst

    if a:
        aa = a.copy()
        b = list(set(lst) - set(a))
        bb = b.copy()

        print(a, 'and', b)
    if k >= 6:
        return
    a.append(lst[k])
    ba(k + 1)
    a.pop()
    ba(k+1)

ba(1)
