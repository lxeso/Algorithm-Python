# 나는야 포켓몬 백준 1620번
# 입력 : 
# 첫째 줄 : 도감에 있는 포켓몬 수 N(1<=N<=100,000), 맞춰야하는 문제의 개수 M(1<=M<=100,000)
# 둘째 줄 - N개의 줄 : 포켓몬 번호가 1-N번에 해당하는 포켓몬의 이름이 한 줄에 하나씩 영어 문자열로 입력됨 (첫글자 대문자, 나머지 소문자, 일부의 경우 마지막 글자 대문자, 길이 2-20)
# M개의 줄 : 내가 맞춰야하는 문제가 입력으로 들어옴. 알파벳 -> 포켓몬 번호 출력. 숫자 -> 포켓몬 이름 출력
# 출력 : M개의 줄에 각각의 문제에 대한 정답을 출력 (포켓몬 이름 -> 포켓몬 번호(숫자) 출력. 숫자 -> 포켓몬 이름 출력)

import sys
input = sys.stdin.read

data = input().splitlines()
N, M = map(int, data[0].split())

# 포켓몬 이름을 -> 번호로 {name: num}
name_to_num = {}

# 포켓몬 번호를 -> 이름으로 {num : name}
num_to_name = {}

# 포켓몬 이름 입력 처리
for i in range(1, N + 1):
    name = data[i]
    name_to_num[name] = i
    num_to_name[i] = name

# 문제 처리
result = []
for i in range(N + 1, N + 1 + M):
    exam = data[i]
    if exam.isdigit():  # 숫자인 경우
        result.append(num_to_name[int(exam)])
    else:  # 문자인 경우
        result.append(str(name_to_num[exam]))

print('\n'.join(result))