# !!!! 주의 !!!!
# 반드시 정렬된 상태에서 이진 탐색을 진행해야 한다.

def binary_search(arr, lo, hi, key):
    # 중간 위치 선택
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)
print(binary_search(arr, 0, N - 1, 67))
print(binary_search(arr, 0, N - 1, 68))

#=======================================================

def binary_search_recur(arr, lo, hi, key):
    if lo >= hi: return -1
    mid = (lo + hi) >> 1
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search_recur(arr, lo, mid - 1, key)
    else:
        return binary_search_recur(arr, mid + 1, hi, key)


arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)
print(binary_search_recur(arr, 0, N - 1, 67))
print(binary_search_recur(arr, 0, N - 1, 68))