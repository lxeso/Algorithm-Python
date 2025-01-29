# 백준 2644번 촌수 계산- 그래프 탐색 (DFS/BFS)

'''
문제 조건
우리나라에서는 촌수라는 개념이 있음. 부모와 자식 사이가 1촌, 할아버지와 손자 사이가 2촌과 같이 촌수를 계산함.  
두 사람의 번호가 주어질 때, 두 사람 사이의 촌수를 구하는 문제.  
만약 두 사람이 전혀 연결되지 않은 경우 -1을 출력해야 함.

## 2. 입력과 출력
[입력]  
1. 첫째 줄: 전체 사람 수 n (1 ≤ n ≤ 100)  
2. 둘째 줄: 촌수를 계산해야 하는 두 사람의 번호  
3. 셋째 줄: 부모-자식 관계 개수 m  
4. 넷째 줄부터: 부모-자식 관계를 나타내는 두 번호 (부모 번호, 자식 번호)

[출력]  
- 두 사람 사이의 촌수를 출력 (경로가 없으면 -1)
'''

'''
알고리즘 설계
1. **그래프 입력받기**
   - `graph = [[] for _ in range(n+1)]` 리스트를 사용하여 인접 리스트 방식으로 그래프 구현
   - `graph[부모].append(자식)`, `graph[자식].append(부모)` (양방향 그래프처럼 만들어야 연결 가능)
  
2. **BFS 탐색 (최단 거리)**
   - `queue`를 사용하여 시작점에서 목표까지 촌수를 계산 (최단 거리 찾기)
   - 방문한 노드는 `visited` 리스트로 관리

'''

from collections import deque

def bfs(start, target):
    queue = deque([(start, 0)])  # (현재 노드, 촌수)
    visited[start] = True

    while queue:
        node, count = queue.popleft()

        # 목표 노드에 도달하면 촌수 반환
        if node == target:
            return count

        # 연결된 노드 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))

    return -1  # 도달할 수 없는 경우 -1 반환

# 입력 받기
n = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 촌수 계산해야 하는 두 사람
m = int(input())  # 부모-자식 관계 개수

# 그래프 초기화
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 입력받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 단방향이지만, 연결을 쉽게 하기 위해 양방향처럼 구현

# BFS 실행
result = bfs(a, b)
print(result)