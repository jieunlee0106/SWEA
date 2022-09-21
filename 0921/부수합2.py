arr = [i for i in range(1, 5)]
n = len(arr)
bits = [0] * n

def b(k, cur_sum):
    if k == n :
        print(bits, end = ' ')
        s=  0
        for i in range(n):
            if bits[i] == 1 :
                print(arr[i], end = ' ')
                s += arr[i]
        print('==>', s, cur_sum)
    else:
        bits[k] = 1
        b(k+1, cur_sum + arr[k])

        bits[k] = 0
        b(k+1, cur_sum)

b(0, 0)