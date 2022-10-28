# combination => 치킨 집 개수 M개로 만드는 조합
# dfs 로 '치킨 거리' 구하기
# 마을 치킨 거리 => 모든 조합 중  가장 작은 수
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

all_shop = []
home = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            arr[r][c] = 0
            all_shop.append([r, c])
        elif arr[r][c] == 1:
            home.append([r, c])

shop_combi = list(combinations(all_shop, M))

for s in range(len(shop_combi)):
    pass