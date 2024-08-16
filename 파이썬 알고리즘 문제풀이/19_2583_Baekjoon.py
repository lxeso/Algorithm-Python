# 백준 2583번 '영역 구하기' DFS 사용
# 문제 : M행 N열의 그래프에서 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇개의 분리된 영역의 개수로 나뉘어지는지 출력
# 입력 첫째 줄 : M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 
# 입력 둘째 줄 : K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다
# 출력 : 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력

import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def dfs(x, y):
    # 방문 처리
    visited[x][y] = True
    # 영역 크기 계산하는데 사용
    area_size = 1
    # 상, 하, 좌, 우 방향 리스트
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
            area_size += dfs(nx, ny)
    return area_size

# 입력
data = input().split()
M, N, K = map(int, data[:3]) # data[:3] = data[0] + data[1] + data[2]
rectangles = [list(map(int, data[i:i+4])) for i in range(3, len(data), 4)]

# 그래프 초기화
graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

# 직사각형의 위치를 1로 설정
for x1, y1, x2, y2 in rectangles:
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

areas = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            areas.append(dfs(i,j))

print(len(areas))
print(' '.join(map(str, sorted(areas))))