# 완전탐색 - 깊이 우선 탐색 알고리즘
# 스택을 이용한 DFS 알고리즘 코드 구현

def dfs_stack(graph, start_node):

    # 기본은 항상 두개의 리스트를 나눠서 관리해주는 것
    need_visited, visited = list(), list()

    # 시작 노드 정하기
    need_visited.append(start_node)

    # 아직 방문이 필요한 노드가 있는 한 반복
    while need_visited:

        # 그 중 가장 마지막 데이터 추출 (스택 구조 활용)
        node = need_visited.pop()

        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:

            # 방문 목록에 추가하기
            visited.append(node)

            # 그 노드에 연결된 노드를
            need_visited.append(graph[node])
    return visited

def dfs_recursive(graph, start, visited = []):
    # 함수 정의: dfs_recursive라는 이름의 함수는 세 개의 인자를 받습니다.
    # graph: 탐색을 수행할 그래프를 나타냅니다.
    # start: 탐색을 시작할 노드를 나타냅니다.
    # visited: 이미 방문한 노드들을 저장하는 리스트로 기본값은 빈 리스트입니다.
    if visited is None:
        visited = []
    visited.append(start)
    # 현재 노드를 방문한 노드 리스트에 추가합니다.
    # 시작 노드(start)를 방문했으므로 visited 리스트에 추가합니다.

    for node in graph[start]:         
        # 현재 노드(start)의 인접 노드들을 하나씩 순회합니다.
        # graph[start]는 시작 노드와 연결된 모든 노드들의 리스트입니다.

        if node not in visited:  # 만약 인접 노드가 방문한 노드 리스트에 없다면 (즉, 아직 방문하지 않았다면)
            dfs_recursive(graph, node, visited)
            # 재귀적으로 dfs_recursive 함수를 호출하여 인접 노드를 방문합니다.
            # 이때 현재의 visited 리스트를 그대로 전달하여 이미 방문한 노드를 기억합니다.
    return visited




graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']