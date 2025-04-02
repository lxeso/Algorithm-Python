# 백준 25192번 인사성 밝은 곰곰이

'''
알고리즘
1. ENTER가 나올 때마다 닉네임 집합(set)을 초기화
2. ENTER 이후에 등장하는 처음 보는 닉네임마다 +1
3. set을 사용해 중복 체크 및 관리
'''

import sys
input = sys.stdin.readline

N = int(input())
nickname_set_list = set()
sum = 0 

for _ in range(N):
    chat = input().strip()

    if chat=="ENTER":
        nickname_set_list = set() # 새로운 사람 입장 -> 기록 초기화
    else: # 채팅 메시지일 경우
        if chat not in nickname_set_list: # 새로운 사람 입장 후 한번도 메시지를 보내지 않은 사용자의 경우
            sum += 1 # 곰곰티콘 사용
            nickname_set_list.add(chat) # 곰곰티콘 사용한 사용자 리스트에 추가

print(sum)

'''
1. 'ENTER' → used_nicknames 초기화 → set()
2. 'pjshwa' → 처음 등장 → greet_count = 1, set = {'pjshwa'}
3. 'chansol' → 처음 등장 → greet_count = 2, set = {'pjshwa', 'chansol'}
4. 'chogahui05' → 처음 등장 → greet_count = 3, set = {'pjshwa', 'chansol', 'chogahui05'}
5. 'ENTER' → 새로운 사람 입장 → set 초기화
6. 'pjshwa' → 다시 처음 보는 걸로 간주 → greet_count = 4, set = {'pjshwa'}
7. 'chansol' → 처음 등장 → greet_count = 5, set = {'pjshwa', 'chansol'}
'''

'''
알아야할 함수 및 문법
set() : 중복 없는 자료를 저장할 때 사용하는 집합. add() → 값 추가. in 연산자 → 포함 여부 확인

'''