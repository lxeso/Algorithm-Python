# 백준 1874번 스택 수열
# 문제 조건 : 스택의 특성(LIFO)을 이용해 하나의 수열을 만들 수 있다.
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
target_list = [int(input().strip()) for _ in range(n)] # 인덱스는 0부터 x-1까지 존재
target_index = 0
answer_list = []
stack = deque() # 스택 생성

for i in range(1,n+1): # 1부터 n까지
    stack.append(i)
    answer_list.append('+')

    while stack and target_list[target_index] == stack[-1]: # 타켓 숫자랑 같다면
        stack.pop() # pop으로 빼고 정답 리스트에 '-' 추가
        answer_list.append('-')
        target_index += 1 # 인덱스 한칸 올려서 다음 타켓 숫자로 넘어감


if (target_index != n): # 반복문을 다 돌고 난 후 인덱스가 n에 도달하지 못했으면
    print('NO')  
else:
    for answer in answer_list:
        print(answer)

