arr = 'abc'
n = len(arr)
bits = [0]*n

# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[1] = i
#         for k in range(2):
#             bits[2] = k
#             print(bits)

# def b(k):
#     if k == n:
#         print(bits)
#
#     else:
#         for i in range(2):
#             bits[k] = i
#             b(k+1)
# b(0)
#
# ans = []

def b(k):
    if k == n:
        print(bits)

    else:
        bits[k] = 0
        b(k+1)

        bits[k] = 1
        b(k+1)

b(0)