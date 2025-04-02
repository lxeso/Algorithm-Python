# 백준 2039번 뱀 찾기
# 그래프 탐색(BFS/DFS) 문제
# 문제 조건 : 0과 1로 차있는 nxm 크기의 격자에서 1들의 연속은 뱀이다. 1이 들어있는 칸 == 뱀 격자.
# 문제 조건 : 뱀의 시작점과 끝점을 제외하고 뱀 안에 있는 뱀 격자는 동서남북 방향으로 2개의 뱀 격자와 만난다. 위의 조건을 만족하는 뱀들 중, 뱀의 양 끝 중 한 군데에 1을 추가시킨다면 더 이상 위의 조건을 만족시키지 않는 것이 maximal snake다.
# 출력 : nxm 격자가 주어져 있을 때, 몇 개의 maximal snake가 있는지 구하는 프로그램을 작성해라
# 입력 : 첫째 줄에 n, m이 주어진다. 그리고 n+1 줄에 걸쳐 격자의 정보가 주어진다.
# Maximal Snake : 현재 뱀(1의 연결 구조)에 추가적인 1을 붙이면, 뱀의 규칙(각 내부 격자는 반드시 2개와 연결)이 깨지는 경우! 즉, 더 이상 확장할 수 없는 상태
'''
📌 주어진 격자 정보 (n x m 크기)
0과 1로 이루어진 격자(grid)
1이 연속적으로 연결된 것이 "뱀"
뱀의 양 끝을 제외하면 항상 "2개의 뱀 격자"와 연결
📌 "Maximal Snake"란?
뱀을 더 연장할 수 없는 상태!
즉, 끝에서 추가적인 1을 붙이면 "뱀이 깨지는" 경우
쉽게 말하면 "연결된 1들의 덩어리 중에서 가장 긴 연결 단위"를 찾는 문제!
'''

'''
1. 입력을 받아서 격자(grid)를 저장한다.
2. 방문 여부를 체크할 visited 배열을 만든다.
3. 2차원 배열을 탐색하면서, 아직 방문하지 않은 1을 발견하면 DFS를 실행한다.
4. DFS를 실행하면서 "현재 뱀"의 모든 격자를 탐색하고, 방문 처리한다.
5. 탐색이 끝나면 "새로운 뱀"을 찾았다고 간주하고 maximal_snake 개수를 증가시킨다.
6. 최종적으로 maximal_snake 개수를 출력한다.

쉽게 다시 정리하자면,
1. 2차원 배열을 하나씩 돌면서 1을 찾는다.
2. 1을 찾았으면 "새로운 뱀"으로 간주하고 탐색 시작!
3. DFS/BFS로 연결된 1들을 전부 방문하면서 "하나의 뱀"을 끝까지 탐색!
4. 탐색이 끝나면 "뱀 개수"를 하나 증가!
5. 위 과정을 반복해서 전체 뱀 개수를 출력!
'''

import sys
sys.setrecursionlimit(10**6) # 재귀 한도 증가

# 상하좌우 이동을 위한 리스트
dx = [-1, 1, 0, 0] # 위, 아래
dy = [0, 0, -1, 1] # 왼쪽, 오른쪽

def dfs(x, y):
    # DFS를 사용해서 (x, y) 위치에서 연결된 모든 1을 탐색
    visited[x][y] = True # 현재 위치 방문처리

    for i in range(4): # 상하좌우 네 방향으로 이동
        nx, ny = x + dx[i], y + dy[i]

        # 범위 내부고, 방문 안했고, 1인 경우 DFS 진행
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)

# 입력 처리
input = sys.stdin.readline
n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 최대 뱀 개수
maximal_snake = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]: # 새로운 뱀 발견
            dfs(i, j) # DFS 실행 
            maximal_snake += 1

print(maximal_snake)