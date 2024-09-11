# 백준 14502번 '연구소' BFS 또는 DFS
# 문제 : 바이러스 확산을 막기 위해 연구소에 벽을 세우려고 한다. 연구소는 크기가 NxM인 직사각형으로 나타낼 수 있으며, 1x1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다. 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하시오.
# 입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.
# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다. 
from itertools import combinations
from collections import deque
import copy # 연구소의 상태를 복사하기 위한 copy 라이브러리

# 바이러스를 퍼뜨리는 함수 : BFS를 사용하여 상후좌우로 바이러스를 퍼뜨림
def spread_virus(lab, N, M):
    # 상하좌우로 이동하기 위한 방향 설정 (위, 아래, 왼쪽, 오른쪽)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque() # BFS를 위한 큐 초기화

    # 연구소에서 바이러스(숫자 2)의 위치를 찾아 큐에 삽입
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2: # 바이러스가 있는 위치이면
                queue.append((i, j)) # 바이러스의 위치를 큐에 추가

    # 큐에 더 이상 퍼뜨릴 위치가 없을 때까지 반복 (BFS)
    while queue:
        x, y = queue.popleft() 
        
        #상하좌우로 바이러스를 퍼뜨리기
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # 새로운 바이러스 퍼뜨릴 좌표 계산

            # 새 좌표가 연구소 범위 내에 있고, 빈 칸(숫자 0)이면 바이러스를 퍼뜨림
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2 # 바이러스로 바꿈
                queue.append((nx, ny)) # 새로운 바이러스 위치를 큐에 넣음

# 연구소에서 안전한 영역(바이러스가 퍼지지 않은 영역)의 크기를 계산하는 함수
def calculate_safe_area(lab, N, M):
    safe_area = 0 # 안전영역의 크기를 저장할 변수
    # 연구소의 모든 칸을 순회하면서
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0: # 빈 칸(숫자 0)이면
                safe_area += 1 # 안전 영역의 크기를 1 증가
    return safe_area # 안전영역의 크기를 반환

def solution():
    # 연구소의 세로 N과 가로 M을 입력받음
    N, M = map(int, input().split()) # N : 연구소의 세로 크기, M : 연구소의 가로 크기
    lab = [list(map(int, input().split())) for _ in range(N)] # 연구소의 상태를 입력받아 lab 배열에 저장 (숫자 0: 빈 칸, 1: 벽, 2: 바이러스)

    empty_spaces = [] # 빈 공간(숫자 0)의 좌표를 저장할 리스트

    # 연구소의 모든 좌표를 순회하면서 빈 칸의 좌표를 수집
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0: # 빈 칸이면
                empty_spaces.append((i, j)) # 빈 칸의 좌표를 리스트에 저장
    
    max_safe_area = 0 # 안전 영역의 최대 크기를 저장할 변수

    # 빈 칸들 중에서 3개의 위치에 벽을 세우는 모든 경우의 수를 구함 (조합)
    for walls in combinations(empty_spaces, 3):
        # 현재 연구소 상태를 복사 (원본 연구소 상태를 변경하지 않기 위함)
        temp_lab = copy.deepcopy(lab)

        # 선택된 3개의 벽을 임시 연구소에 세움
        for x, y in walls:
            temp_lab[x][y] = 1 # 선택된 빈 칸을 벽(숫자 1)으로 바꿈
        
        # 바이러스를 퍼뜨림 (벽을 세운 후의 상태에서 바이러스 확산)
        spread_virus(temp_lab, N, M)

        current_safe_area = calculate_safe_area(temp_lab, N, M)

        max_safe_area = max(max_safe_area, current_safe_area)
    
    print(max_safe_area)




solution()





'''
문제 전문

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

'''