
arr = [1,2, 2, 3, 4 ,5]
lst =[]
def back(s, n, r):

    if r == n:
        print(lst)
        return
    for i in range(s, 6):
        lst.append(arr[i])
        back(i+1, n, r - 1)
        lst.pop()

back(0, 3, 6)