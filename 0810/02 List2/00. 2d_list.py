# 2차 배열 생성
# 초기값 0으로 채원진 3 x 3 배열 생성할 때 주의하세요.

arr1 = [[0] * 3] * 3
arr1[0][0] = 10
print(arr1)

arr2 = [[0] * 3 for _ in range(3)]
arr2[0][0] = 10
print(arr2)
