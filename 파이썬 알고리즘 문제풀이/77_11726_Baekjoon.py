# 백준 11726 2xn 타일링
'''
문제
2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램 작성하시오
입력 : n 이 주어짐
출력 : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
dp[n] = 2xn 크기의 직사각형을 채우는 방법의 수

2로 세로 크기는 고정, 가로 크기만 생각했을 때 매번 채울 수 있는 방법은 단 2가지임
1. 가로로 1칸 차지 : 2x1 타일 1개 사용 |
2. 가로로 2칸 차지 : 1x2 타일 2개 사용 = (남은 채우는 가로로가 2칸 이상일때만 가능)
매번 1번, 2번 두 경우 모두 탐색.. 모든 경우의 수니까..

n == 1
1번 1회
n == 2
1번 2회 dp[2] -> dp[1] -> dp[0]
2번 1회 dp[2] -> dp[0] 
=> 총 2회
n == 3
1번 3회 dp[3] -> dp[3-1=2] -> dp[2-1=1] -> dp[1-1=0]
1번 1회 + 2번 1회 dp[3] -> dp[3-1=2] -> dp[2-2=0]
2번 1회 + 1번 1회 dp[3] -> dp[3-2=1] -> dp[1-1=0]
n == 4
1번 4회 dp[4] -> dp[4-1=3] -> dp[3-1=2] -> dp[2-1=1] -> dp[1-1=0]
1번 1회 + 2번 ㅜ회 dp[4] -> dp[4-2=2] ->  

즉, n을 -1 혹은 -2를 해서 0을 만들 수 있는 경우의 수 (순서 중요) 
재귀는 메모리 초과 날것 같고.. 타뷸레이션 방식? 1부터 채움. 어차피 다른 곳에서 더할 dp[3] 
'''



def solution():
    N = int(input())
    dp = [0] * (N+1)
    for i in range(N+1):
        if i == 1:
            dp[1] = 1 # dp[1] = 1 + dp[0] = 1
        elif i == 0:
            dp[0] = 0
        elif i == 2:
            dp[2] = 2
        else: # 
            dp[i] = dp[i-1] + dp[i-2]
            '''
            dp[3] = dp[2] + dp[1] = 2 + 1 = 3
            3 = -1-1-1, -2-1, -1-2
            dp[4] = dp[3] + dp[2] = 3 + 2 = 5
            4 = -1-1-1-1, -1-2-1, -2-1-1, -1-1-2, -2-2
            '''
    result = dp[N] % 10007
    print(result)



#11727번 2xn 타일링 2
'''
2xn 크기의 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수를 구하는 프로그램 작성하시오
입력 : n 이 주어짐
출력 : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
dp[n] = 2xn 크기의 직사각형을 채우는 방법의 수
'''
def solution_11727():
    N = int(input())
    dp = [0]*(N+1)
    result = 0
    for i in range(N+1):
        if i == 0:
            dp[0] = 0
        elif i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 3 # 1x2 2개, 2x1 2개, 2x2 1개
        else: # 2보다 클 때
            dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
    print(dp[N] % 10007)



def solution_1316(): # 그룹단어 1316번
    n = int(input())
    count = 0

    for _ in range(n):
        word = input().strip()
        seen = set() # 지금까지 나온 문자들
        prev = '' # 이전 문자 저장용
        is_group = True # 그룹 단어인지 체크하는 플래그

        for char in word:
            if char != prev:
                if char in seen:
                    is_group = False 
                    break
                seen.add(char)
            prev = char # 이전 문자 업데이트
        if is_group:
            count += 1
    print(count)

def solution_1920():
    import sys
    input = sys.stdin.readline
    N = int(input())
    n_list = list(map(int, input().strip().split())) # n_list = [4, 1, 5, 2, 3]
    M = int(input())
    m_list = list(map(int, input().strip().split())) # m_list = [1, 3, 7, 9, 5]
    n_list.sort()
    answer_list = [0] * M
    for i, m in enumerate(m_list):
        start = 0
        end = N-1
        mid = (start + end) // 2
        while start <= end:
            if n_list[mid] > m:
                end = mid - 1
            elif n_list[mid] < m:
                start = mid + 1
            elif n_list[mid] == m:
                answer_list[i] = 1
                break
    print('\n'.join(answer_list))

        
def solution_25206():
    import sys
    input = sys.stdin.readline
    dict = {
        'A+': 4.5,
        'A0' : 4,
        'B+' : 3.5,
        'B0' : 3.0,
        'C+' : 2.5,
        'C0' : 2.0,
        'D+' : 1.5,
        'D0' : 1.0,
        'F' : 0.0
    }
    total_sum = 0
    p_count = 0
    for _ in range(20):
        name, score, rate = map(str, input().strip().split())
        if score == 'P':
            p_count += 1
        total_sum += score * dict.get(rate, 0)
    answer = total_sum / (20-p_count)
    print(answer)

def solution_5217():
    import sys
    input = sys.stdin.readline

    T = int(input())
    answer = []
    for _ in range(T):
        n = int(input())
        print(f"Pairs for {n}:", end = " ")
        for i in range(1, (n+1)//2):
            j = n-i
            if i < j:
                answer.append(f"{i} {j}")
        print(", ".join(answer))

def solution_10093():
    import sys
    input = sys.stdin.readline
    A, B = map(int, input().strip().split())
    if A >= B:
        big = A
        small = B
    else:
        big = B
        small = A
    print(big-small-1)
    for i in range(small+1, big):
        print(i, end = " ")

def solution_15000():
    letters = input().strip()
    letters.upper()
    print(letters.upper())

def solution_20492():
    N = int(input())
    print(int(N-(N * 0.22)), int(N-((N*0.2)*0.22)))
solution_20492()