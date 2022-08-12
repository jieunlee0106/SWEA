#strlen() 함수 구하기

def strlen(arr):

    i = 0
    while arr[i] != '\0':
        i += 1
    return i


arr = ['s', 's', 'a', 'f', 'y', '\0']
print(strlen(arr))

'''
뒤집기
mystr = 'algorithm'


#파이썬 내장기능
print(arr[::-1])

#새로운 공간에 저장
rev_str = ''
for i in range(len(my_str) -1, -1, -1):
    rev_str += mystr[i]
print(rev_str)
    '''
#
# #교환을 통해서 뒤집기
# my_str = 'algorithm'
# my_str = list(my_str)
# for i in range(len(my_str)//2):
#     N = len(my_str)
#     my_str[i], my_str[N-1-i] = my_str[N-1-i], my_str[i]
# print(''.join(my_str))

"""s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'


print(s1 is s1) #True
print(s1 is s2) #True => id값이 같아
print(s1 is s3) #False
print(s1 is s4) #True
print(s1 is s5) #False

print(s1 == s1) #True
print(s1 == s2) #True
print(s1 == s3) #False
print(s1 == s4) #True
print(s1 == s5) #True

print(s1 is s5) #False"""

#int 사용하지 않고 문자를 숫자로

def itoa(num):
    pass

    #0의 아스키 코드 값에 문자열 더해서
    #문자열 얻어서 이어붙이기

val = itoa(1234)
print(type(val), val)