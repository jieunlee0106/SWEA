nj = []
for _ in range(9):
    nj.append(int(input()))
nj = sorted(nj)
nine_nj = sum(nj)
out = nine_nj - 100

for i in range(9):
    for j in range(i, 9):
        if i != j:
            nn = nj[i] + nj[j]
            if nn == out:
                out1 = nj[i]
                out2 = nj[j]
                nj.remove(out1)
                nj.remove(out2)
                break
            break
print(*nj, sep='\n')
