# tree = [0, 4, 2, 6, 1, 3, 5]
# n = len(tree)
# last = n-1
# lst = []
# def inorder(v):
#     if v > last: return
#
#     inorder(v*2)
#     lst.append(tree[v])
#     inorder(v*2+1)
# inorder(1)
# print(lst)

# 이진트리는 자식이 0인지 아닌지 판단 할 필요가 없다
def inorder(v):
    global num
    if v > n: return
    inorder(v*2)
    h[v] = num
    num += 1
    inorder(v*2+1)

for t in range(int(input())):
    n = int(input())
    num = 1
    h = [0] * (n + 1)
    inorder(1)

    print(f'#{t+1}', h[1], h[n//2])