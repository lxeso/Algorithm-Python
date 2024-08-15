# 2468번 백준 '안전 영역' 2차원 리스트 DFS 사용
# 문제 : 지역에 높이정보가 행과 열의 높이가 각각 N인 2차원 그래프로 주어진다. 많은 비가 내렸을때 물에 잠기지 않는 '안전 영역'이 최대 몇개 만들어지는 지 출력. 
# 안전 영역 : 물에 잠기지 않은 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해있으며 그 크기가 최대인 영역
# 입력 : 첫째 줄 : 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력 (N은 2>=, 100<= 정수) 둘째 줄: N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보( 1이상 100 이하의 정수)가 입력. 
# 출력 : 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
import sys
input = sys.stdin.read
sys.setrecursionlimit(1000000) # 재귀 깊이 기본값 1000에서 1000000로 증가해서 설정

def dfs(x, y, rain_height):
    # 상, 하, 좌, 우 네 방향을 나타내는 방향 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > rain_height:
            visited[nx][ny] = True # 방문 표시
            dfs(nx, ny, rain_height)
def solution(rain_height):
    result_count = 0
    for i in range(N):
        for j in range(N):
            # 방문하지 않았으며, 물 높이보다 높은 지점에서 시작
            if not visited[i][j] and graph[i][j] > rain_height:
                visited[i][j] = True
                dfs(i, j, rain_height)
                result_count += 1
    return result_count

# 입력
data = input().split() # data = ['5', '6', '8', '2', '6', '2', '3', '2', '3', '4', '6', '6', '7', '3', '3', '2', '7', '2', '5', '3', '6', '8', '9', '5', '2', '7']
N = int(data[0]) # data[0] = '5'
graph = [] # 2차원 리스트 저장할 그래프 선언
index = 1
for i in range(N):
    graph.append(list(map(int, data[index:index+N]))) # 첫번째 반복문 -> data[1:6] = ['6', '8', '2', '6', '2']
    index += N

max_safe_areas = 0

#각 물 높이에 대한 안전 영역의 최대 개수 계산
for rain_height in range(max(max(row) for row in graph)+1): # 최대 지역의 높이정보까지 반복
    visited = [[False] * N for _ in range(N)] # 방문 리스트를 모두 False로 초기화하고 시작
    max_safe_areas = max(max_safe_areas, solution(rain_height)) # 최대 안전지역 개수 계속 갱신하며 max_safe_areas에 저장

print(max_safe_areas)