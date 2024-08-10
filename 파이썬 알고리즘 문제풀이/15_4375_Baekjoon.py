# 4375번 백준 1
# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
# 입력 : 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.
# 출력 : 각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
# 접근 방법 : 숫자를 1, 11, 111, 1111 과 같이 키워나가면서 N으로 나눠지는지 따지는 문제 
import sys

def solution(n):
    from collections import deque

    queue = deque(["1"]) # 숫자 1로 시작

    visited = set()

    while queue:
        curr_node = queue.popleft() # 큐에서 현재 숫자를 꺼냄. ## 첫번째 루프에서 "1"

        curr_num = int(curr_node) # 현재 숫자를 정수로 변환 ## "1" -> 1

        if curr_num % n == 0: # 만약 현재 숫자가 n의 배수일때 ## 1이 n의 배수인지 확인
            return len(curr_node) # 각 자리수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력해야 하기 때문에 그 숫자의 자릿수를 반환 -> 자리수만큼의 1의 연속이 원하는 숫자
        
        # 만약 현재 숫자가 n으로 나눠지지 않을 때, 즉 정답이 아직 나오지 않았을 경우

        if curr_node not in visited: # 아직 방문하지 않은 노드라면
            visited.add(curr_node) # 방문 set에 추가 후

            queue.append(curr_node + "1") # 큐에 숫자 "1"을 하나 더 붙인 숫자("11", "111")을 큐에 넣어가며 계속해서 탐색을 진행

input = sys.stdin.read # 모든 입력을 한 번에 읽어옴 [3 \n 7 \n 9901]
data = input().split() # 각 줄마다 주어진 숫자들을 공백으로 구분하여 리스트로 저장

for n in data: # 각 테스트 케이스마다 함수 호출해서 정답 출력
    n = int(n) # 
    if n % 2 != 0 and n % 5 != 0: # n이 2와 5로 나눠 떨어지지 않는 경우만 처리
        result = solution(n) # 정답 함수 호출
        print(result) # [3 \n 6 \n 12]