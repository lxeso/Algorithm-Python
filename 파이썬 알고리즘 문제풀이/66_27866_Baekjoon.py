# 백준 27866번 문자와 문자열
'''
import sys
input = sys.stdin.readline
S = input()
i = int(input())
list = []
print(S[i-1])


# 구분
N = int(input())
numbers = int(input())
sum = 0
for _ in range(N):
    sum += numbers % 10
    numbers = numbers // 10

print(sum)


# 구분

N, X = map(int, input().strip().split())
A = list(map(int,input().split(' ')))
answer = []
for num in A:
    if num < X:
        answer.append(num)
print(*answer)


# 구분

N = int(input())
num_list = list(map(int, input().strip().split()))
print(min(num_list), max(num_list))

# 구분

num_list = []

for i in range(1, 31):
    num_list.append(i)
for _ in range(28):
    num = int(input())
    num_list.remove(num)
    
print(*num_list)


# 3052번 알고리즘 : 중복을 허용하지 않는 set 자료형을 이용해, 42를 나눈 나머지를 전부 set 자료형에 저장시키고, 마지막에 set의 length(길이)를 출력시킴
num = 42
rest_num = set()

for _ in range(10):
    divide_num = int(input())
    rest_num.add(int(divide_num%num))
print(len(rest_num))
'''

# 11021번 문제 입출력
import sys
input = sys.stdin.readline
T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().strip().split(' '))
    print(f"Case #{i}: {A+B}")
