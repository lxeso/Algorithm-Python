# 백준 1012번 유기농 배추 2차원 그래프 문제 (DFS 알고리즘 사용)
# 문제 : 배추에 지렁이가 한마리라도 살고 있으면 지렁이는 인접한 다른 배추로 이동 가능하다. 인접 = 상하좌우. 배추들이 모여있는 곳에는 지렁이가 1마리만 있으면 된다.
# 입력 : 첫 줄에는 테스트 케이스의 개수 T, 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500), 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다
# 출력 : 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력

import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 설정 (DFS를 위해 필요. 안하면 런타임 에러남) 원래는 1000으로 재귀 호출 최대 깊이가 제한되어 있음. 이 한도를 넘어서면 파이썬 인터프리터가 런타임에러 발생 시킴. (스택 오버플로우를 방지하기 위해 설정된 안전장치)
# 설정해줘야 하는 이유 : 배추 밭이 넓고 연결된 배추가 많은 경우 (50X50) -> 재귀호출깊이 : 2500이 되기 때문에 파이썬에서 제한한 1000이 넘어감. 그러므로 따로 다시 한도를 늘리는 설정을 해줘야함

def dfs(x, y, farm, visited, N, M):
    # 현재 위치를 방문 처리
    visited[y][x] = True
    
    # 상, 하, 좌, 우 네 방향을 나타내는 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 네 방향으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # 미로 범위 내에 있고, 배추가 심어져 있으며, 아직 방문하지 않은 곳
        if 0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1 and not visited[ny][nx]:
            dfs(nx, ny, farm, visited, N, M)

def solution():
    T = int(input())  # 테스트 케이스의 수

    for _ in range(T):
        M, N, K = map(int, input().split())  # 가로, 세로, 배추의 수
        farm = [[0] * M for _ in range(N)]  # 배추밭 초기화 (모든 위치에 0으로 초기화)
        visited = [[False] * M for _ in range(N)]  # 방문 여부 기록
        
        # 배추 위치 입력
        for _ in range(K):
            x, y = map(int, input().split())
            farm[y][x] = 1  # 배추가 심어진 위치를 1로 표시
            
        worm_count = 0  # 필요한 배추흰지렁이 수
        
        # 모든 위치를 탐색
        for i in range(N):
            for j in range(M):
                if farm[i][j] == 1 and not visited[i][j]:  # 배추가 심어져 있고 방문하지 않은 위치라면
                    dfs(j, i, farm, visited, N, M)  # DFS로 연결된 모든 배추를 방문 처리
                    worm_count += 1  # 새로운 군집 발견, 배추흰지렁이 수 증가
        
        print(worm_count)  # 결과 출력

# 함수 호출
solution()
