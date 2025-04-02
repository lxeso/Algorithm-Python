# 백준 9012번 '괄호' - 스택
# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
# 입력 
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 
# 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
# 출력
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
# 알고리즘 : 스택 사용
import sys
from collections import deque


def vps(ps):
    stack = []  # 스택을 빈 리스트로 초기화
    for char in ps:
        if char == '(': # 여는 괄호일 경우 스택에 추가
            stack.append('(')
        elif char == ')': # 닫는 괄호일 경우
            if stack: # 스택이 비어있지 않은 경우에만
                stack.pop()
            else:
                print("NO")
                return
    if(len(stack) == 0):
        print("YES")
    else:
        print("NO")

def solution():
    input = sys.stdin.read
    data = input().split()
    test_case = int(data[0])

    for i in range(1, test_case + 1):
        vps(data[i])

# 예제 실행
solution()



# 방법 2
import sys
from collections import deque

input = sys.stdin.read
data = input().split() # data = ['3', '(())', '()()', '((()))']
N = int(data[0])

stack = deque()
for string in data[1:]: # 또는 for string in data[1:N+1]: 
    stack = deque()
    is_vps = True # VPS 여부 저장하는 변수
    for char in string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack: #if len(stack) == 0:
                print("NO")
                is_vps = False
                break
            stack.pop()
        
    if is_vps and not stack:
        print("YES")
    elif is_vps:
        print("NO")


'''
모르는 것 
1. data[0]이 테스트케이스 개수고, data[1~N]까지가 접근해야 할 문자열일때, for문을 어떻게 쓰는가? data[1:N+1]
2. 오른쪽 괄호가 나와서 스택에서 pop을 하려고 하는데 스택이 이미 비어있다면? vps가 아니므로 'NO'를 출력해야 하는데..? 미리 스택이 비어져있는지 확인 후 pop 시도
3. 함수가 아닌 상태에서 return을 사용할 수 없으니 출력 부분이 중복되어 일어나는건 어떻게 해결? is_vps = True 변수로 깃발처럼 활용해 해결.. 하지만 최적의 방식은 결국 함수를 따로 만들고 return을 활용하는 방식
4. data[1:N+1]의 정확한 범위 : 1이상 ~ N+1 미만!! (N+1) 포함 안됨!
'''
 
# 3번째 풀이 시도

import sys
from collections import deque

def is_vps_func(ps):
    stack = deque() # 스택 생성
    for char in ps:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack: # 빈리스트 == false 반환. 즉 스택이 비어있다면
                print('NO')
                return
            stack.pop()
    if not stack:
        print('YES')
        return
    else:
        print('NO')
        return

input = sys.stdin.read
data = input().strip().split()
ts_num = int(data[0])

for ps in data[1:]:
    is_vps_func(ps)


