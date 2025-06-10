# 1463번 1로 만들기 DP 동적계획법
'''
1로 만들기
1. x가 3으로 나눠지면 3으로 나눔
2. X가 2로 나눠지면 2로 나눔
3. 1 뺌
위의 세가지 연산만 사용해서 1을 만들어야됨. 연산을 사용하는 횟수의 최솟값을 출력해라

무조건 반복됨.
예를 들어 10은 2로 나누면 5가 되고, 5의 결과를 더해주기만 하면 됨.
dp[n] = n일때 1로 만드는 연산 최소 횟수
1 : 아무것도 안함. 0 반환
2 : 2로 나눔 
3 : 3으로 나눔
4 : 2로 나눔=2 + dp[2]
5 : 1 뺌 + dp[4]
6 : 3으로 나눔 + dp[2]
7 : 1을 뺌 + dp[6]
8 : 2로 나눔 + dp[4]

즉, 2 또는 3으로 나눠지면 d[n]에서 + d[n//2] 혹은 + d[n//3]
2와 3으로도 안나눠지면 -1 연산 1회 추가해서 d[n]에서 1 + d[n-1]
'''
# 재귀는 top-down 방식.. for문 반복문으로 1부터 채우기
# 아 뭔가 내 방식이 죄적이 아니구나..
import sys
sys.setrecursionlimit(10**6)


def top_down(n): # 문제.... '최소' 조건이 충족이 안됨 -> 들어가는 방법마다 min으로 비교해서 더 적은거 리턴하게..? 재귀 너무 많이 쓰여서 메모리 다 잡아먹는거 아님?
    N = int(input())

    dp = [-1] * (N+1) # dp = [0, 0, 0, ... , 0] 초기 세팅값 전부 -1

    
    # 만약 n이 10일때
    if dp[n] != -1: # 만약에 이미 계산되었으면 메모이제이션 이미 저장한거 리턴..
        return dp[n]
    
    if n == 1:
        dp[1] = 0
        return 0
    elif n == 2:
        dp[2] = 1
        return 1
    elif n == 3:
        dp[3] = 1
        return 1
    
    if (n % 3 == 0): # n = 6 들어감
        dp[n] =  min(1 + top_down(n//3), 1 + top_down(n-1)) # dp[6] = 1 + solution(2) = 2
        return dp[n]
    elif (n % 2 == 0): # n = 10 들어감 n = 4 들어감 1 + solution(2) = 1 + 1 = 2
        dp[n] = min(1 + top_down(n//2), 1 + top_down(n-1)) #  dp[6] = 1 + solution(5) = 1 + 3 = 4
        return dp[n] # dp[10] = 1 + solution(5) = 3
    else: # 2와 3으로 안나눠질때는 무조건 1을 빼는 연산으로 감
        dp[n] = 1 + top_down(n-1) # dp[5] = 1 + solution(4) = 1 + 2 = 3
        return dp[n]


def bottom_top():
    N = int(input())
    dp = [0] * (N+1)
    
        
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i//2])
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i//3])
    print(dp[N])