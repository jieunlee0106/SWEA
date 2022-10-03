N = 4
arr = [i + 1 for i in range(N)]
cnt = 0
pick = []
def backtrack(k, cur_sum, num): # K: 현재 노드의 높이, 함수 호출 깊이, k번 선택을 한 상태
    # k번 원소에 대한 선택==> cur_sum에는 0 ~ k-1 원소들에 대한 선택이 계산
    if k == N:
        global cnt
        cnt += 1
        print(pick, sum(pick), cur_sum)
    else:
        # k번 원소를 포함
        pick.append(arr[k])
        backtrack(k + 1, cur_sum + arr[k], num + 1)
        pick.pop()
        # k번 원소를 미포함
        backtrack(k + 1, cur_sum, num)

backtrack(0, 0, 0); print('cnt= ', cnt)
