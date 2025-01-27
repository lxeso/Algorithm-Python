# 백준 1260번 DFS와 BFS

'''
문제 정의
그래프를 DFS와 BFS 방식으로 탐색한 결과를 출력하는 프로그램을 작성하는 문제.
특정 정점부터 시작해 연결된 정점을 정해진 순서(번호가 작은 순서)로 방문하며, 각각의 탐색 결과를 출력해야 한다.

[입력]
1. 첫 줄에 정점 개수 N, 간선 개수 M, 시작 정점 번호 V가 주어짐.
2. 다음 M개의 줄에 간선을 연결하는 두 정점 번호가 주어짐 (양방향 그래프).
[출력]
1. 첫째 줄에 DFS를 수행한 결과.
2. 둘째 줄에 BFS를 수행한 결과.
'''

'''
알고리즘
1. 그래프 입력받기
입력받은 M개의 간선을 기반으로 인접 리스트를 생성.
각 정점에서 연결된 정점들을 번호 순으로 방문하기 위해 정렬.
2. DFS 구현
재귀를 이용하여 구현.
visited 리스트를 사용해 방문 여부를 확인.
정점 번호가 작은 순서대로 방문하기 위해 인접 리스트를 미리 정렬.
3. BFS 구현
큐를 이용하여 구현.
방문할 정점을 큐에 추가하고, 큐에서 꺼낸 정점을 기준으로 다시 인접 정점들을 방문.
'''

from collections import deque

def dfs(graph, visited, node, result):
    visited[node] = True
    result.append(node)  # 방문한 노드 추가
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 방문하지 않은 이웃 탐색
            dfs(graph, visited, neighbor, result)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])  # BFS는 큐를 사용
    visited[start] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:  # 방문하지 않은 이웃 큐에 추가
                visited[neighbor] = True
                queue.append(neighbor)
    return result

# 입력 처리
n, m, v = map(int, input().split())  # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n + 1)]  # 1-index 기반 그래프

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순으로 방문하기 위해 정렬
for edges in graph:
    edges.sort()

# DFS 탐색
visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(graph, visited_dfs, v, dfs_result)

# BFS 탐색
bfs_result = bfs(graph, v)

# 결과 출력
print(*dfs_result)
print(*bfs_result)
