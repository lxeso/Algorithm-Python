# 팰린드롬인지 확인하기 10988번
# 알파벳 소문자의 단어가 팰린드롬인지 확인 (앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말함)
# 입력 : 단어 (알파벳 소문자로 이루어져 있고 길이는 1~100)
# 출력 : 팰린드롬이라면 1, 아니면 0 출력

word = input() # 입력받은 단어를 for 문으로 돌려서 알파벳 하나하나 검사 list[i] = list[end-i] 여기서 end는 list의 마지막 인덱스, i는 0부터 시작해서  end의 반만큼 돌음
end = len(word)-1 # 마지막 인덱스

result = 1 # 기본값 1로 설정

for i in range (len(word)//2):
    if word[i] != word[end-i]: #조건문 만족할경우, 즉 팰린드롬이 아닐 경우 result 0으로 만들고 반복문 빠져나가서 출력
        result = 0 
        break

print(result)

word2 = input()

if word == word[::-1]: # 파이썬의 슬라이싱(slicing) 기능을 사용해서 문자열을 뒤집어서 비교. word[::-1] - 전체 문자열을 뒤집는 슬라이싱
    print(1)
else:
    print(0)