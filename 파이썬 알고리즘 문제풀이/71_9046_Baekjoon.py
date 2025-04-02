
# 백준 9046번 복호화
import sys
from collections import Counter
def solution_9046():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        sentence = input() # 공백+소문자 알파벳으로 이루어진 암호문 입력받음
        filtered_sentence = [ch for ch in sentence if ch.isalpha() and ch.islower()] #알파벳 소문자만 필터링해서 리스트에 추가
        counter = Counter(filtered_sentence) # counter = {'a': 2, 'b' : 3, 'c' : 1}
        common = counter.most_common() # common = [('b', 3), ('a', 2), ('c', 1)] # 내림 차순 정렬

        if not common: # 만약 common이 빈리스트라면, 아무것도 없다면 오류이므로 '?' 출력하고 즉시 반복 종료 후 다음 반복으로 넘어가게 continue 적어줌
            print('?')
            continue
        
        result_num = 0
        max_freq = common[0][1]
        for char, freq in common:
            if max_freq == freq:
                result_num += 1
        if result_num == 1:
            print(common[0][0])
        else:
            print('?')

solution_9046()

def solution_1():
    word = sys.stdin.readline() # word = 'BaekjoonOnlineJudge'
    count = 0
    for char in word:
        count += 1 
        if count < 10:
            print(char, end = "")
        else:
            count = 0
            print(char, end = "\n")
def solution_2():
    for 