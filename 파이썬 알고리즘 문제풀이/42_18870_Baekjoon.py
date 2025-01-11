# 백준 18870번 좌표 압축
'''
[문제 설명]
N개의 정수 좌표가 주어질 때, 좌표를 압축하여 상대적인 크기를 표현하시오.
좌표 압축이란, 모든 좌표를 정렬한 뒤, **작은 값부터 0, 1, 2, ...** 순으로 번호를 부여하는 과정입니다.
중복된 값은 같은 번호를 가지며, 좌표 간의 간격은 고려하지 않습니다.

[입력]
1. 첫 번째 줄: 좌표의 개수 N
2. 두 번째 줄: 공백으로 구분된 N개의 정수 좌표

[출력]
1. 원래 순서대로 압축된 좌표 값을 출력.
2. 값들은 공백으로 구분

'''

'''
<알고리즘 설명>
1. 입력받기
   - 첫 번째 줄에서 좌표의 개수 N을 입력받음.
   - 두 번째 줄에서 좌표 리스트 original를 입력받음.

2. 중복 제거 후 정렬
   - original에서 중복을 제거하고 값을 정렬하여 sorted_unique 리스트 생성.

3. 값과 순서를 매핑
   - `bisect_left`를 이용해 각 좌표 값의 정렬된 위치(인덱스)를 찾아 번호를 매김.

4. 압축된 좌표 리스트 생성
   - 각 original 값에 대해 `bisect_left`로 번호를 찾고, 이를 새로운 리스트에 저장.

5. 결과 출력:
   - 리스트를 공백으로 구분하여 출력.
'''

import bisect

def coordinate_compression(original):
    # 중복 제거 후 정렬
    sorted_unique = sorted(set(original))
    
    # 좌표 압축 수행
    compressed = [bisect.bisect_left(sorted_unique, x) for x in original]
    return compressed

# 입력 처리
N = int(input())  # 좌표 개수
original = list(map(int, input().split()))  # 원래 좌표 리스트

# 좌표 압축 실행
result = coordinate_compression(original)

# 결과 출력
print(" ".join(map(str, result)))
