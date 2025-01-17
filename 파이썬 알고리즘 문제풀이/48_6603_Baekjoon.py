# 백준 6603번 로또 - 백트래킹
'''
문제 조건

49가지 수 중 6개를 골라야 하는데,
유명한 로또 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것임.
집합 S와 k가 주어졌을 때, '수를 고르는 모든 방법'을 출력하는 프로그램을 작성해야함
한마디로 순열 공식? kC6

[입력]
입력은 여러개의 테스트 케이스로 이루어져 있음. 첫번째 수는 k(6<k<13)이고, 다음 k개의 수는 집합 S에 포함되는 수임. S의 원소는 오름차순으로 주어짐
[출력]
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력함
각 테스트 케이스 사이에는 빈 줄을 하나 출력해야함
'''

'''
알고리즘
1. 입력받기
    a. 여러 줄로 주어지는 입력을 한꺼번에 받아야 하므로 `sys.stdin.read`를 사용해 전체 데이터를 읽음.
    b. 읽어온 데이터를 `split("\n")`으로 각 줄을 분리해 리스트 `data`에 저장.
    c. `data`에서 각 줄을 하나씩 처리하며, `line == "0"`일 때 반복 종료.

2. 입력 데이터 처리
    a. 각 줄에서 숫자를 공백 기준으로 나눠 리스트로 변환.
    b. 첫 번째 값은 `k`로 저장 (숫자 개수).
    c. 나머지 숫자들은 집합 `S`로 저장.

3. 백트래킹 함수 호출
    a. `backtracking(S, start, path)` 형태로 호출.
    b. `start`는 현재 숫자의 탐색 시작 위치, `path`는 현재 선택된 숫자 조합을 저장하는 리스트.

4. 백트래킹 함수 작성
    a. 종료 조건: `path`의 길이가 6이 되면 조합을 완성했으므로 출력하고 반환.
    b. 반복문: `for i in range(start, len(S))`로 현재 인덱스 이후의 숫자만 선택하도록 탐색 범위를 제한.
    c. 재귀 호출: `backtracking(S, i + 1, path + [S[i]])`로 선택된 숫자를 `path`에 추가하고 다음 탐색 시작 위치를 `i + 1`로 설정.

5. 출력 형식 유지
    a. 각 테스트 케이스의 결과 뒤에 빈 줄을 추가해 출력 형식 유지.
    b. 빈 줄 출력은 `print()`를 사용.

6. 코드 종료
    a. `line == "0"`을 만나면 반복을 종료해 프로그램 종료.
'''

import sys
input = sys.stdin.read
data = input().strip().split("\n")


def backtracking(S, start, path):
    # 종료 조건: path의 길이가 6이 되면 출력
    if len(path) == 6:
        print(*path)
        return
    
    # 현재 인덱스 이후의 숫자만 탐색
    for i in range(start, len(S)):
        backtracking(S, i + 1, path + [S[i]])




for line in data:
    if line == "0": #입력이 0이라면 종료
        break
    numbers = list(map(int, line.split())) # 숫자 리스트로 변환
    k = numbers[0]
    S = numbers[1:] # 나머지는 집합 S
    backtracking(S, 0,[])
    print()