import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().strip().split())

    result = a + b

    print(result)

if __name__ == '__main__':
    main()

# ----------------------------

import sys
import itertools

input = sys.stdin.readline

def main():
    n, r = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))

    comb_list = list(itertools.combinations(numbers, r))

    for comb in comb_list:
        print(' '.join(map(str, comb)))


# ----------------------------

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().strip().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1]) # 합 배열에서 구간합 구하기

# -----------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())


arr = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)

# -----------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
S = [0] * N
C = [0] * M
S[0] = A[0]
answer = 0

for i in range(1, N):
    S[i] = S[i-1] + A[i] # 합배열 저장

for i in range(N):
    remainder = S[i] % M # 합 배열의 모든 값에 % 연산 수행
    if remainder == 0:
        answer += 1
    C[remainder] += 1


# -----------------------------------------

from collections import deque
















