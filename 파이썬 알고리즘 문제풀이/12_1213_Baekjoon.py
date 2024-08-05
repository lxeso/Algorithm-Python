# 백준 1213번 팰린드롬 만들기
# 입력 : 영어 단어가 입력되면 순서를 적절히 바꿔 팰린드롬으로 출력. 알파벳 대문자로만 된 최대 50글자 ex) "AABB"
# 출력 : 팰린드롬으로 바꾼 단어 출력. 불가능할 경우 "I'm Sorry Hansoo"를 출력. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력 ex) "ABBA"

def solution(word):
    from collections import Counter

    counter = Counter(word) # 홀수일 경우.. 만약 홀수인 알파벳이 2개 이상이면 실패. 홀수인 알파벳이 1개이거나 0개여야함

    odd_count = 0
    odd_char = ''

    for char, count in counter.items():
        if count % 2 != 0: # 홀수라면
            odd_count += 1 # 카운트를 올림
            odd_char = char
        if odd_count >= 2: #만약 홀수인 알파벳이 2개 이상이면 실패
            return "I'm Sorry Hansoo"

    first_half = []
    for char in sorted(counter.keys()):
        first_half.append(char * (counter[char] // 2))
    first_half = ''.join(first_half)

    if odd_count == 1:
        full_palindrome = first_half + odd_char + first_half[::-1]
    else:
        full_palindrome = first_half + first_half[::-1]
    
    return full_palindrome

word = input()
print(solution(word))