# 백준 3986번 좋은 단어
# 최적 알고리즘 : 스택
# A와 B로만 이루어진 단어(2이상, 100,000이하)에서, 같은 글자끼리 단어 위로 아치형 곡선을 그어 쌍을 지었을때, 선끼리 교차하지 않으면서 각 글자를 정확히 한개의 다른 위치에 있는 글자와 짝 지을 수 있다면, '좋은 단어'로 평가
# 입력 : 첫째 줄에 단어의 수 N이 주어짐(1이상, 100이하). 다음 N개의 줄에는 A와 B로만 이루어진 단어가 한ㅈ 줄에 하나씩 주어짐
# 출력 : 첫째 줄에 좋은 단어의 개수를 출력

def solution(word_list):
    answer = 0
    for word in word_list: # word_list = ["ABAB", "AABB", "ABBA"] 
        answer += is_good_word(word)
    return answer

def is_good_word(word):
    stack = []
    result_count = 0
    for char in word:
        if stack and stack[-1] == char: # 만약 stak이 비어있지 않고, 현재 문자가 스택의 마지막 요소와 일치할 때
            stack.pop() # 마지막 문자 꺼내서 삭제
        else: # 스택이 비어있거나, 스택의 마지막 요소와 일치하지 않을때
            stack.append(char) # 현재 문자 스택에 추가
    if len(stack) == 0: # 모든 반복문 돌고 난 후, 스택이 비어있다면 '좋은 단어'
        return 1
    else:
        return 0  


N = int(input())
word_list = [input().strip() for _ in range(N)]
print(solution(word_list))