# 백준 1182번 부분수열의 합 - 백트래킹

'''
문제 정의
N개의 정수로 이루어진 수열에서, 크기가 1이상인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 출력하는 프로그램을 작성
[입력]
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어짐. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. (주어진 정수의 절대값) < 100,000
[출력]
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력 (순서x 중복x)
'''

'''
알고리즘
1. N, S를 map(int, input().strip().split()) 입력받기.
2. N_list를 list(map(int, input().strip().split())) 로 입력받음
3. N_list를 정렬해야되야 할까요?
4. backtracking(N, N_list, S, visited, path ) 함수 호출
5. backtracking 함수 작성
5-1. 종료 조건 sum_of_path(path 리스트안의 모든 요소의 합)이 S가 될 때 count = count + 1하고 return
? count를 어디서 초기화하지? 인덱스로 보내줘야하나?
5-2. for 반복문 시작. for i, num in enumerate(N_list):  i는 인덱스, num은 요소
5-2. 탐색 제한 조건 : sum_of_path > S인 순간 탐색할 필요 없음.
5-3. backtracking 재귀 호출 전 visited[i]를 True로 설정해주고 재귀 호출한 다음 다시 False로 복귀시켜줌
'''


def backtracking(index, current_sum):
    global count

    # 모든 숫자를 확인했으면 종료
    if index == N:
        return

    # 현재 숫자를 포함한 경우
    if current_sum + N_list[index] == S:  # 합이 S가 되면 카운트
        count += 1

    # 현재 숫자를 포함하는 경우 탐색
    backtracking(index + 1, current_sum + N_list[index])

    # 현재 숫자를 포함하지 않는 경우 탐색
    backtracking(index + 1, current_sum)


# 입력 받기
N, S = map(int, input().strip().split())
N_list = list(map(int, input().strip().split()))

count = 0  # 합이 S가 되는 경우의 수
backtracking(0, 0)  # 초기값: 인덱스 0, 현재 합 0
print(count)
