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
1. N과 S를 map(int, input().strip().split())으로 입력받음
2. N_list를 list(map(int, input().strip().split()))로 입력받음
3. count 변수를 0으로 초기화
4. backtracking(index, current_sum) 함수를 작성하고, backtracking(0, 0) 호출
5. backtracking 함수 작성
5-1. 종료 조건: index가 N과 같아지면 탐색 종료
5-2. current_sum이 S와 같고, 선택된 원소가 1개 이상일 경우 count += 1
5-3. 현재 인덱스 숫자를 포함하는 경우: backtracking(index + 1, current_sum + N_list[index]) 호출
5-4. 현재 인덱스 숫자를 포함하지 않는 경우: backtracking(index + 1, current_sum) 호출
6. 모든 탐색이 끝난 후 count를 출력
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
