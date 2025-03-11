# 백준 1110번 더하기 사이클 (구현 문제)

import sys

input = sys.stdin.readline

N = int(input())
result = N
count = 0

while(True):
    left = result // 10 # 왼쪽 숫자(몫)
    right = result % 10 # 오른쪽 숫자(나머지)
    right_second = (left + right) % 10 # 다음 숫자의 오른쪽 숫자(나머지)
    result = (right*10) + right_second # 오른쪽 숫자와 다음 숫자의 오른쪽 숫자를 조합해서 새로운 숫자를 만듦
    count = count + 1
    if (N == result): # 원래의 수와 일치하면 반복문 깨고 나감
        break
    

print(count)