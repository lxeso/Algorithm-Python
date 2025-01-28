# 백준 2606번 바이러스 - 그리디
'''
문제 조건
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 네트워크를 통해 감염되는 컴퓨터의 수를 구해야 한다.
(단, 1번 컴퓨터는 제외하고 계산.)
'''

'''
알고리즘
1. 그래프 입력받기
컴퓨터 간 연결 관계를 기반으로 인접 리스트 형태의 그래프를 생성한다.
컴퓨터 번호가 1번부터 시작하므로, 크기가 N+1인 리스트를 생성해 인덱스를 맞춘다.
2. DFS 탐색
DFS를 이용해 1번 컴퓨터에서 연결된 모든 컴퓨터를 탐색한다.
방문한 컴퓨터를 기록하기 위해 visited 리스트를 사용한다.
3. 감염된 컴퓨터 수 계산
DFS로 탐색한 컴퓨터 수에서 1번 컴퓨터를 제외한 개수를 계산한다.
'''

def dfs(graph, start, visited):
    visited[start] = True
    count = 1  # 현재 컴퓨터를 감염된 컴퓨터로 추가
    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)  # 연결된 컴퓨터를 재귀적으로 탐색
    return count


# 입력 처리
n = int(input())  # 컴퓨터 수
m = int(input())  # 간선 수
graph = [[] for _ in range(n + 1)]  # 인접 리스트로 그래프 생성

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 방문 기록
visited = [False] * (n + 1)

# 1번 컴퓨터에서 시작해 감염된 컴퓨터 수 계산
infected_count = dfs(graph, 1, visited) - 1  # 1번 컴퓨터 제외
print(infected_count)
