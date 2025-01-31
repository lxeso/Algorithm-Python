# 백준 5014번 스타트링크 - BFS
'''
문제 조건
1. **엘리베이터 버튼을 최소 몇 번 눌러야 목표 층 G에 도착할 수 있는지 찾기.**
2. **이동 방법**
    - U 버튼을 누르면 현재 층에서 U층 위로 이동
    - D 버튼을 누르면 현재 층에서 D층 아래로 이동
    - U층 위 또는 D층 아래로 이동할 수 없는 경우 엘리베이터는 움직이지 않음.
3. **목표 층 G에 도달할 수 없는 경우** `"use the stairs"` 출력해야 함.

[입력]

1. **첫 번째 줄** :`F S G U D` (공백 구분)
    - `F` (1 ≤ F ≤ 1,000,000) : 건물의 총 층 수
    - `S` (1 ≤ S ≤ F) : 현재 위치한 층
    - `G` (1 ≤ G ≤ F) : 목표 층
    - `U` (0 ≤ U ≤ 1,000,000) : 한 번에 위로 올라갈 수 있는 층 수
    - `D` (0 ≤ D ≤ 1,000,000) : 한 번에 아래로 내려갈 수 있는 층 수

[입력]

1. 목표 층 `G`에 도달할 수 있으면 **최소 버튼 클릭 횟수 출력**
2. 목표 층 `G`에 도달할 수 없으면 `"use the stairs"` 출력
'''

'''
알고리즘 설계
- **입력 받기**
    - `F`: 전체 층 수
    - `S`: 현재 위치 (시작 층)
    - `G`: 목표 층
    - `U`: 위로 갈 수 있는 층 수
    - `D`: 아래로 갈 수 있는 층 수
- **BFS 탐색을 수행하여 최소 버튼 횟수 찾기**
    - `queue`를 사용하여 현재 위치와 버튼을 누른 횟수를 저장.
    - `visited` 리스트를 사용하여 이미 방문한 층을 다시 방문하지 않도록 처리.
    - `U` 버튼과 `D` 버튼을 사용하여 이동할 수 있는 층을 탐색하며 목표 층 `G`에 도달하면 버튼 횟수 출력.
- **엘리베이터로 도착할 수 없는 경우 "use the stairs" 출력**
    - BFS를 끝까지 실행했음에도 `G` 층에 도달하지 못하면 `"use the stairs"` 출력.
'''

from collections import deque

def bfs(F, S, G, U, D):
    queue = deque([(S, 0)])  # 현재 층, 버튼 누른 횟수
    visited = [False] * (F + 1)  # 방문 체크 리스트
    visited[S] = True  # 시작 층 방문 처리

    while queue:
        current, count = queue.popleft()

        # 목표 층 도달 시 버튼 횟수 출력
        if current == G:
            return count

        # 위로 이동
        if current + U <= F and not visited[current + U]:
            queue.append((current + U, count + 1))
            visited[current + U] = True

        # 아래로 이동
        if current - D >= 1 and not visited[current - D]:
            queue.append((current - D, count + 1))
            visited[current - D] = True

    return "use the stairs"  # 도달할 수 없는 경우

# 입력 처리
F, S, G, U, D = map(int, input().split())

# BFS 실행
print(bfs(F, S, G, U, D))
