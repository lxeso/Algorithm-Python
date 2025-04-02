# 백준 20920번 영단어 암기는 괴로워

'''
알고리즘
1. 모든 단어를 입력받아 빈도수 세기 (collections.Counter 사용)
2. 길이가 M 이상인 단어만 필터링
3. 정렬 기준을 다음과 같이 설정하여 정렬
    - 빈도수 내림차순 (-freq)
    - 길이 내림차순 (-len(word))
    - 알파벳 오름차순 (word)
4. 정렬된 순서대로 단어 출력
'''

import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

filtered_words = [] # ['apple', 'sand', 'apple', 'append', 'sand', 'sand']
for word in words:
    if len(word) >= M: # 단어 길이가 M 이상인 경우에만 암기
        filtered_words.append(word)

word_count = Counter(filtered_words) # 단어 등장 횟수 세기 (딕셔너리 형태로 반환) 
# word_count = {'apple': 2, 'sand': 3, 'append': 1}

# 정렬하기 (# items(): 딕셔너리의 key-value 쌍을 튜플로 반환)
word_items = list(word_count.items()) # word_items = [('apple', 2), ('sand', 3), ('append', 1)]

def sorting(item):
    word = item[0]
    count = item[1]
    return (-count, -len(word), word) # 작은것 -> 큰것이 기본이므로, 자주 나오는 단어(-count), 단어 길이가 길수록(-len), 알파벳 사전순으로(기본)
    # 결과튜플 : (-2, -5, 'apple') (-3, -4, 'sand') (-1, -6, 'append')
'''
1. -count 기준 → 숫자가 클수록 앞으로 (실제로는 횟수가 많을수록)
    → sand(3), apple(2), append(1)
2. count가 같으면 -len(word) → 길이가 길수록 앞으로
3. 그것도 같으면 word 자체로 → 알파벳 순
'''
sorted_words = sorted(word_items, key=sorting) # sorted_words = [('sand', 3), ('apple', 2), ('append', 1)]

for item in sorted_words:
    print(item[0])
'''
sorted() 함수는 파이썬에서 리스트를 정렬해주는 함수. 기본 정렬은 [작은것 -> 큰것]
sorted()의 동작 흐름 : 리스트 안에 있는 각 요소(하나씩)를 key=정렬기준함수에 넣어보고, 그 결과를 기준으로 정렬하는 것. 즉, word_items 리스트에서 하나씩 꺼내서 → sorting(item)에 넣음
sorted(리스트, key=함수) # key=함수 옵션으로 직접 '정렬기준함수'를 작성해서 정렬 가능.
조건이 1개일땐 'key=len'과 같이 간단하게 작성가능하지만, 정렬 기준이 여러개일 경우 정렬 기준들을 '튜플'로 묶어서 반환하게 하는 함수를 작성

# 점수 높은 순 → 이름 알파벳 순
def 기준(student):
    이름 = student[0]
    점수 = student[1]
    return (-점수, 이름)  # 마이너스를 붙이면 높은 점수가 먼저 나옴

print(sorted(students, key=기준))

'''