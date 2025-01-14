# 백준 15651번 N과 M(3) - 백트래킹
'''
문제 조건
자연수 N과 M이 주어졌을때, 1부터 N까지 자연수 중 중복 가능하게 M개를 고른 수열들을 출력하는 프로그램 작성
[입력]
첫째 줄에 자연수 N과 M이 주어짐 (1 ≤ M ≤ N ≤ 7)
[출력]
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력.
중복되는 수열을 여러번 출력하면 안되며, 각 수열은 공백으로 구분하여 출력
수열은 사전 순으로 증가하는 순서로 출력해야함.
'''

'''
알고리즘
1. N과 M을 입력받음
2. 백트래킹 함수 backtracking 작성
3. visited는 N+1만큼 False를 생성하고, backtracking 함수에 인자로 N, M, visited, path를 보내줌
4. backtracking 함수에서는, 우선 종료 조건을 써줌. 종료 조건은 path 리스트의 length가 M이 될때임. 이 조건 만족할 시 print(*path) 써주고 바로 return
4-1. 그리고 for i in range(1, N + 1)까지 반복해서 재귀로 backtracking(N, M, path + [i], visited)를 다시 호출해줌. 
'''

def backtracking(N, M, path):

    if len(path) == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        backtracking(N, M, path + [i])    

N, M = map(int, input().strip().split())

backtracking(N, M, [])
