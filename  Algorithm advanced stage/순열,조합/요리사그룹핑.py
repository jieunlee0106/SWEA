arr = [1, 2, 3, 4]
n = 4

def back(k):
    if k == n:
        if len(a) == 2:
            print(a, b)
        pass

    else:
        a.append(arr[k])
        back(k+1)
        a.pop()
        b.append(arr[k])
        back(k+1)
        b.pop()

a = [arr[0]]
b = []
back(1)