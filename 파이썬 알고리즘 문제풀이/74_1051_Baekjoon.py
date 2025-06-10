# 백준 1051번 숫자 정사각형 - 완전탐색 (브루트포스 문제)

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))
grid = [list(input().strip()) for _ in range(M)]
max_size = 0
for i in range(N):
    for j in range(M):
        for k in range(min(N, M)): # NxM의 직사각형 안에서 나올 수 있는 최대 크기의 정사각형은 NxN 혹은 MxM 중 작은 것임
            if (i+k) <= N and (j+k) <= M:
                if grid[j][i] == grid[j+k][i] == grid[j][i+k] == grid[j+k][i+k]:
                    square = (k+1) ** 2
                    max_size = max(max_size, square)


print(max_size)
