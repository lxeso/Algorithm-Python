# 백준 26069번 붙임성 좋은 총총이

'''
알고리즘
1. 무지개 댄스를 추는 사람들을 set으로 저장
2. 기록을 순서대로 읽으면서:
    - 둘 중 한 명이라도 댄스 추면 두 사람 모두 set에 넣어줌
3. 마지막에 set의 길이 출력
'''

import sys
input = sys.stdin.readline

N = int(input())
dance_people = set()
dance_people.add("ChongChong")
for _ in range(N):
    A, B = input().strip().split(' ')
    if (A in dance_people) or (B in dance_people):
        dance_people.add(A)
        dance_people.add(B)

print(len(dance_people))


'''
#이전 풀이
N = int(input())
dance_people = set()

for _ in range(N):
    A, B = input().strip().split(' ')
    if A == "ChongChong" or B == "ChongChong":
        dance_people.add(A)
        dance_people.add(B)
    if (A in dance_people) or (B in dance_people):
        dance_people.add(A)
        dance_people.add(B)

'''