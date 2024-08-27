# 카카오테크 부트캠프 8월 코딩테스트 3번문제
# 트리 구조에서 최대한 다양한 노드를 탐방하는 문제. 트리에서 두 노드 사이의 경로가 항상 유일하다는 성질을 이용하여, 가장 긴 경로(지름)를 찾는 문제로 변환 가능. 이를 해결하기 위해 **트리의 지름(Tree Diameter)**을 구하는 방법을 사용
# 즉, 트리의 지름을 구해야함
import sys  # 시스템에서 입력을 받을 때 사용
from collections import defaultdict, deque  # defaultdict는 기본 값을 가지는 딕셔너리, deque는 양쪽에서 삽입과 삭제가 빠른 큐

def dfs(node, graph, visited):
    stack = [(node, 0)]  # DFS를 위한 스택 초기화. 각 항목은 (노드 번호, 현재까지의 거리)로 구성됨
    farthest_node = node  # 가장 먼 노드를 현재 노드로 초기화
    max_distance = 0  # 가장 먼 거리 초기화

    while stack:  # 스택이 빌 때까지 반복
        current_node, current_distance = stack.pop()  # 스택에서 현재 노드와 거리를 꺼냄
        if visited[current_node]:  # 이미 방문한 노드라면 건너뜀
            continue
        visited[current_node] = True  # 현재 노드를 방문했다고 표시

        if current_distance > max_distance:  # 현재 노드까지의 거리가 지금까지의 최대 거리보다 크다면
            max_distance = current_distance  # 최대 거리를 갱신
            farthest_node = current_node  # 가장 먼 노드를 갱신

        # 현재 노드에 연결된 이웃 노드들에 대해 반복
        for neighbor in graph[current_node]:
            if not visited[neighbor]:  # 아직 방문하지 않은 이웃 노드에 대해서만
                stack.append((neighbor, current_distance + 1))  # 이웃 노드를 스택에 추가, 거리도 1 증가시킴

    return farthest_node, max_distance  # 가장 먼 노드와 그 노드까지의 거리를 반환

def solution():
    input = sys.stdin.read  # 표준 입력에서 모든 줄을 읽어옴
    data = input().splitlines()  # 각 줄을 리스트의 원소로 분리함

    N = int(data[0])  # 첫 번째 줄에서 맛집의 개수(노드의 개수)를 가져옴
    if N == 1:  # 만약 맛집이 하나라면
        print(1)  # 최대 탐방할 수 있는 맛집 개수는 1이므로 바로 출력하고 종료
        return

    graph = defaultdict(list)  # 그래프를 인접 리스트로 표현하기 위한 딕셔너리 초기화
    for i in range(1, N):  # 두 번째 줄부터 N번째 줄까지 반복
        u, v = map(int, data[i].split())  # 두 맛집(노드)의 번호를 읽어옴
        graph[u].append(v)  # u번 맛집과 v번 맛집이 서로 연결되었다고 그래프에 기록
        graph[v].append(u)  # 양방향 그래프이므로 반대 방향도 기록

    # 첫 번째 DFS: 임의의 노드에서 가장 먼 노드를 찾기 위해 1번 노드부터 시작
    visited = [False] * (N + 1)  # 각 노드의 방문 여부를 기록하기 위한 리스트 초기화
    farthest_node, _ = dfs(1, graph, visited)  # 1번 노드에서 시작하여 가장 먼 노드와 그 거리를 찾음

    # 두 번째 DFS: 첫 번째 DFS에서 찾은 가장 먼 노드에서 다시 시작하여 가장 먼 노드를 찾음
    visited = [False] * (N + 1)  # 방문 리스트를 다시 초기화
    _, max_distance = dfs(farthest_node, graph, visited)  # 가장 먼 노드에서 시작하여 트리의 지름을 구함

    print(max_distance)  # 최종적으로 트리의 지름(가장 먼 거리)를 출력

# 예제 실행
solution()

'''
문제

구름이는 맛집 탐방이라는 취미를 가지고 있다. 그래서 역시 오늘도 맛집 탐방을 하러 어느 한 도시에 도착했다.
도착한 도시에는 N개의 맛집이 있고, 맛집마다 1번부터 N번까지 차례대로 번호가 부여되어 있다. 또한, 서로 다른 두 맛집 사이를 잇는 N - 1개의 길이 있다. 이때, 어떤 두 맛집을 선택해도 선택한 두 맛집 사이에는 단순 경로가 유일하다. 단순 경로란, 경로상 중복된 맛집이 없는 경로를 의미한다.
구름이는 임의의 맛집을 정해 거기서 시작해 길을 통해 이동하면서 탐방하려고 한다.
이때, 도착한 모든 맛집은 반드시 지나치지 않고 방문해야 한다. 물론, 탐방을 시작한 맛집도 포함이다. 그런데 구름이는 최대한 다양한 맛집을 탐방하고 싶어하지만, 동시에 최대한 효율적으로 탐방을 하고 싶어한다. 그래서 이미 방문한 맛집을 다시 방문하지 않게끔 탐방하려고 한다.
구름이가 이미 방문한 맛집을 다시 방문하지 않으면서 최대한 다양한 맛집을 탐방할 때, 탐방할 수 있는 맛집의 최대 개수를 알아보자.

출력

구름이가 이미 방문한 맛집을 다시 방문하지 않으면서 최대한 다양한 맛집을 탐방할 때, 탐방할 수 있는 맛집의 최대 개수를 출력한다

'''
