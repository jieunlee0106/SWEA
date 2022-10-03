a = [3, 1, 5, 22 , 8, 4, 23, 0]
def sol(a):
    n = len(a)

    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if a[j] < a[mini]:
                mini = j
        a[mini], a[i] = a[i], a[mini]
sol(a)
print(a)