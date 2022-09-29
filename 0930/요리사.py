from itertools import combinations
def DISH():

for tc in range(1, int(input())+1):
    n = int(input())
    lst= [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    dish = []
    for i in combinations(lst, n//2):
        dish += [[i]]
        DISH()