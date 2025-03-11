# 백준 10813번 나이순 정렬
# 문제 조건 : 가입한 순으로 가입한 사람의 (나이, 이름)가 주어짐. 이때 회원들의 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램 작성
# 알고리즘 : 입력받는 순서 그대로 리스트에 괄호 쌍으로 (나이, 이름) 저장,  그 상태에서 나이로만 재정렬 (안정정렬)


import sys
input = sys.stdin.readline

N = int(input())
people = []

for _ in range(N):
    age, name = input().strip().split()
    people.append((int(age), name)) # 나이는 정수형으로 꼭 변환해줘야함

people.sort(key = lambda x: x[0])

for age, name in people:
    print(age, name)