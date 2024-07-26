# 농구 경기 백준 1159번
# 입력 : 선수의 수 N (1~150), N개의 줄에 각 선수의 성이 주어짐
# 출력 : 선수 다섯명 선발 가능 시 : "PREDAJA", 불가능 시 : 선발 가능한 선수의 첫글자를 사전순으로 공백없이 모두 출력
# 성의 첫 글자가 같은 선수 5명 선발. 만약 성의 첫글자가 같은 선수가 5명 미만이라면, 기권 => "PREDAJA" 출력
from collections import Counter

N = int(input())
first_name_list = [input() for _ in range (N)]
first_alphabet = [first_name[0] for first_name in first_name_list]


# 방법 두가지 1. Counter 함수 사용하기 2. ord 함수 사용하기

# 1. Counter 함수 사용하기
 
counter = Counter(first_alphabet) # 알파벳 개수 세기

#만약 숫자 카운트 중 5가 넘어가는게 있으면 해당 알파벳 모두 반환
result = []

for char in range(ord('a'), ord('z')+1):
    if counter[chr(char)] >= 5:
        result.append(chr(char))

if len(result) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(result))) # 결과 리스트를 공백 없이 문자열로 변환하여 출력
    
    
# 두번째 풀이
# 입력 받기
N = int(input())
first_names = [input().strip()[0] for _ in range(N)]
# 첫 글자의 빈도 계산
counter = Counter(first_names)

result = [char for char, count in counter.items() if count >= 5]

if result:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")