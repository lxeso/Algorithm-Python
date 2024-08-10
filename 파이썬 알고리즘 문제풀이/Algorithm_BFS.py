# BFS (너비 우선 탐색 알고리즘)
# 그래프에서 시작 노드에 인접한 노드부터 탐색. 인접한 노드를 반복적으로 큐에 삽입하고 먼저 삽입된 노드부터 차례로 큐에서 꺼냄
# 1. 탐색 시작 노드 정보를 큐에 삽입하고 '방문 처리' 한다.
# 2. 큐에서 노트를 꺼내 방문하지 않은 인접 노드 정보를 모두 큐에 삽입 후 '방문 처리'
# 3. 2번 과정을 수행할 수 없을 때까지 반복 
from collections import deque


'''
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
'''

def bfs_dic(start_node, graph): # graph가 dictionary일 때
    queue = deque([start_node]) # 현재 노드 꺼내기
    visited = set([start_node]) # 현재 노드 방문 set에 

    while queue:
        curr_node = queue.popleft() # 맨 앞에 요소 삭제

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return -1

'''
    graph = [
        ['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
    ]
'''

def bfs_2DArray(start_x, start_y, graph): # graph가 2D Array 일 때
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, -1]

    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return -1

