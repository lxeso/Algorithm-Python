# 일곱 난쟁이
# 1. 9줄의 난쟁이들의 숫자(키)) 입력받기
# 2. 9개의 숫자 중 합이 100이 되는 7개의 숫자(키) 조합해서 찾아내기 (완전탐색-9개의 숫자 중 7개의 숫자를 선택하여 합이 100이 되는지 확인)
# 3. 숫자(키)를 오름차순으로 출력하기
import sys
from itertools import combinations

input_data = sys.stdin.read() # 모든 입력을 한 번에 읽어 들이기

heights = list(map(int, input_data.split())) # 각 줄을 분리하고 정수로 변환하여 리스트에 저장

pick_seven = combinations(heights, 7) # 9개 중 7개를 선택하는 모든 조합 생성

for current_pick_seven in pick_seven:
    if sum(current_pick_seven) == 100:
        result = current_pick_seven
        break

for height in sorted(result):
    print(height)