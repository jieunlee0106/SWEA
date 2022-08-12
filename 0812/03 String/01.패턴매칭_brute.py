#염기서열 (ATGC 네개의 물질)
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)
#텍스트에서 패턴이 존재할 수 있는 모든 시작 위치
for i in range(n-m+1): # 0 ~ n-m
    #i = 매칭할 텍스트의 시작위치
    for j in range(m):
        if p[j] != t[i + j]: # 0 ~ m-1
            break #break없으면 일치했다는 것
    else:
        print(i, t[i:i+m])
