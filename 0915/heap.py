# 최대힙 구하기
size = 100
h = [0]*size
last = 0        # 마지막 노드의 번호, 전체 노드  수


def push(item):
    # full 상태를 체크: last == size-1
    # 마지막 노드의 다음 위치에 저장
    global last
    last += 1
    h[last] = item
    # 부모-자식 간의 대소 관계를 체크
    c, p = last, last//2
    while p > 0 and h[c] > h[p]:        # 부모가 유효한 값인지 확인하고 c가 루트가 아닌 것을 확인하ㅣㄱ 위해 p > 0
        h[c], h[p] = h[p], h[c]
        c = p
        p = p//2      # 부모를 자식으로 / 자식을 부모로

def pop(item):
    # empty check: last == 0
    global last
    ret = h[1]      # 루트 리턴
    h[1] = h[last]      # 마지막 노드를 루트에 복사
    last -= 1           # 마지막 노드 삭제

    p, c = 1, 2 #(p*2)  # 루트, 왼 쪽 자식

    while c <= last:

        if c + 1 <= last and h[c] < h[c+1]:
            c += 1      # c는 왼쪽자식이었는데 만약 오른쪽 자식이 더 크면 c 가 오른쪽 자식을 가르키게

        if h[c] <= h[p]: break    # 바꿀 필요가 없으면

        h[c], h[p] = h[p], h[c]
        c = p
        c = p*2
    return ret
'''   
    while True:
        # 왼쪽 자식이 있는지 체크, 마지막 노드 번호보다 큰 값인지 확인
        if c > last: break # 자식이 없는 경우
        # 오른쪽 자식이 있는지 체크
        if c + 1 <= last and h[c] < h[c+1]:
            c += 1      # c는 왼쪽자식이었는데 만약 오른쪽 자식이 더 크면 c 가 오른쪽 자식을 가르키게
        if h[c] > h[p]:
            h[c], h[p] = h[p], h[c]
            c = p
            c = p*2
        else:
            break
'''


data = [69, 10, 30, 2, 16, 31, 22]

for val in data:
    push(val)

while last > 0:
    print(pop(), end= ' ')