# 백준 15649번 N과 M(1) - 백트래킹
'''
문제 조건 : 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 M개의 숫자를 중복 없이 선택해 모든 가능한 순서를 출력하는 문제
[입력]
첫째 줄에 자연수 N과 M이 주어진다 (1 ≤ M ≤ N ≤ 8)
[출력]
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력해야함
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 함.
수열은 사전 순으로 증가하는 순서로 출력해야함
'''

''' 
알고리즘
1. N(사용할 숫자의 범위)과 M(선택할 숫자의 개수)를 입력 받음.
2. 백트래킹 알고리즘 적용 - 재귀를 이용해 M개의 숫자를 선택. 이미 선택된 숫자는 방문하지 않도록 설정
3. 조건에 맞는 수열 출력 - 선택된 숫자의 길이가 M에 도달하면 결과 출력
'''

def backtracking(N, M, path, visited):
    # 종료 조건 : path 리스트의 길이가 M이면 출력
    if len(path) == M:
        print(*path) # 언패킹 연산자 * 사용
        return
    
    for i in range(1, N+1): # 1부터 N까지 숫자 탐색
        if not visited[i]: # 방문하지 않은 숫자만 선택
            visited[i] = True # 방문 처리
            backtracking(N, M, path + [i], visited) # 다음 단계
            visited[i] = False # 탐색 종류 후 방문 해제

N, M = map(int, input().strip().split())
visited = [False] * (N + 1)
backtracking(N, M, [], visited)