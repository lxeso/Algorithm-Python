# 백준 2108번 통계학

'''
1. **입력 받기**
    리스트에 N개의 정수 저장
    
2. **산술평균**
    `round(sum(nums) / N)` (단, `-0`이 출력되지 않게 `+0` 처리 필요)
    
3. **중앙값**
    정렬 후 `nums[N//2]` 출력
    
4. **최빈값**
    `Counter`로 빈도수 계산 후, **가장 많이 나온 값들 중 두 번째로 작은 값** 출력
    
5. **범위**
    `max(nums) - min(nums)`
'''

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# 정렬
numbers.sort()

# 산술 평균 (반올림) → -0 방지로 +0 해줌
avg = round(sum(numbers) / N) + 0

# 중앙값 (이미 정렬되어있으므로 가운데 인덱스 값임)
mid = numbers[N//2]

# 최빈값
counter = Counter(numbers)  # 각 숫자의 등장 횟수 세기
most_common = counter.most_common()  # [(숫자, 빈도), ...] 형태로 내림차순 정렬됨
max_freq = most_common[0][1]  # 가장 높은 빈도수

# 최빈값 후보만 모으기
modes = [num for num, freq in most_common if freq == max_freq]
modes.sort()

# 조건: 여러 개일 경우 두 번째로 작은 값 출력
mode = modes[0] if len(modes) == 1 else modes[1]

# 6. 범위
range_val = numbers[-1] - numbers[0]

# 7. 출력
print(avg)
print(mid)
print(mode)

print(range_val)

def solution():
    import sys
    data = sys.stdin.readline
    try:
        while True:
            line = input()
            count_list = [0, 0, 0, 0] # 소문자, 대문자, 숫자, 공백 개수
            for char in words:
                if char.islower(): # 알파벳 소문자면
                    count_list[0] += 1
                elif char.isupper(): # 알파벳 대문자면
                    count_list[1] += 1
                elif char.isdigit(): # 숫자면
                    count_list[2] += 1
                elif char == " ": # 공백이면
                    count_list[3] += 1    
            print(' '.join(map(str, count_list)))# join() 함수는 문자열만 다룰 수 있음
    except EOFError:
        pass