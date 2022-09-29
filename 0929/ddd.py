lst = [1, 2, 3, 4, 5, 6]
r = []
r.append([1, 2])
r.append([lst.remove(r[0])])
print(r)