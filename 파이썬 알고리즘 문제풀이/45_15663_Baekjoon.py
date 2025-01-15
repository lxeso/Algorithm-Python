# 백준 15663번 N과 M(9) - 백트래킹
'''
문제 조건
N개의 자연수와 자연수 M이 주어졌을때 그 N개의 자연수 중에서 M개를 선택한 수열을 모두 출력
[입력]
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어짐. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수
[출력]
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
수열을 중복되게 출력해서는 안되고, 각 수열을 공백으로 구분해서 출력해야함.
수열은 사전 순으로 증가하는 순서로 출력
'''

'''
알고리즘
1. N, M을 map(int, input().strip().split())으로 입력받음.
2. N_list를 list(map(int, input().strip().split()))으로 입력받고 정렬함 (사전 순으로 출력하기 위해).
3. visited 리스트를 False로 N만큼 채워서 선언함.
4. backtracking 함수에 N, M, visited, path, N_list를 보내줌.
5. backtracking 함수 작성.
   5-1. 종료 조건: path 리스트의 길이가 M과 일치하면 print(*path) 출력 후 return으로 종료.
   5-2. 반복문 시작: N_list에서 하나씩 선택 -> for i, num in enumerate(N_list).
   5-3. 중복 제거: 현재 숫자(num)가 이전 숫자와 같고, 이전 숫자가 탐색되지 않은 상태(not visited[i-1])라면 건너뜀.
   5-4. 선택한 숫자의 인덱스를 visited[i]로 True 설정해서 방문 처리.
   5-5. 재귀 호출: backtracking(N, M, visited, path + [num], N_list).
   5-6. 복구: visited[i]를 다시 False로 설정.
'''

def backtracking(N, M, visited, path, N_list):
    if len(path) == M:
        print(*path)
        return
    
    for i, num in enumerate(N_list):
        if i > 0 and N_list[i - 1] == N_list [i] and not visited[i-1]:
            continue
        if not visited[i]:
            visited[i] = True
            backtracking(N, M, visited, path + [num], N_list)
            visited[i] = False


N, M = map(int, input().strip().split())
N_list = list(map(int, input().strip().split()))
N_list.sort() # 사전 순 출력 위해
visited = [False] * N
backtracking(N, M, visited, [], N_list)