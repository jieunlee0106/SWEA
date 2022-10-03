import copy
arr = [1, 2, 3]
ret = []
def back(subset, i, arr):
    if i == len(arr):
        ret.append(copy.copy(subset))
        return
    else:
        subset.append(arr[i])
        i += 1
        back(subset, i, arr)
        subset.pop()
        back(subset, i, arr)
back([], 0, arr)
print(ret)