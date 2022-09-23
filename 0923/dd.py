from itertools import product
n = 5
cnt_lst = [cc for cc in range(1, n - 1)]
ans = []
for i in (product(cnt_lst, repeat=2)):
    ans.append(list(i))
ans.remove([n - 2, n - 2])
for i in range(len(ans)):
    ans[i].extend([ans[i][0], ans[i][1]])
print(ans)