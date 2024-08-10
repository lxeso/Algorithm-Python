# 그래프(미로)를 입력받는 방법 
# N : 행의 수, M : 열의 수
'''
입력
4 6 (행, 열)
101111
101010
101011
111011
'''

'''
결과 (2차원 리스트 형태인 그래프)
graph = [ 
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1] 
]
'''

# 방법 1 : 기본 input() 함수 사용
def inputGraph_2D_list(): # 2차원 리스트로 저장하는 방법 (직관적이고 이해가 쉽지만 입력이 커질 시 속도가 느려짐. 초보자에게 적합한 방법)
    N, M = map(int, input().split()) 

    graph = [] # 그래프를 저장할 리스트

    for _ in range(N):
        row = list(map(int, input())) # 한 행(가로)을 '숫자'의 리스트로 변환 [1, 0, 1, 1, 1, 1]
        graph.append(row) # 리스트를 리스트에 추가. 리스트 안에 리스트, 즉 2차원 리스트가 되어 [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0]] 와 같은 형식으로 추가됨
    


# 방법 2 : sys.stdin.read()를 사용한 전체 입력 받아서 분리
def inputGraph_sys(): # sys.stdin.read() 사용 (대량의 입력을 빠르게 처리할 수 있어 효율적이지만 모든 입력을 한 번에 받아서 처리해야 하므로 유연성이 떨어질 수 있음)
    import sys

    input_data = sys.stdin.read().splitlines() # 행과 열, 그래프를 한꺼번에 입력 받아 전체 입력을 줄 단위로 나누어 리스트로 만듦 
    # input_data = ['4 6', '101111', '101010', '101011', '111011']

    N, M = map(int, input_data[0].split()) # 첫 번째 줄에서 N과 M을 추출
    #  input_data[1:] : 슬라이싱(slicing) 문법을 사용하여 리스트 input_data에서 첫 번째 요소(즉, '4 6')를 제외한 나머지 부분을 가져옴
    #  input_data[1:] = ['101111', '101010', '101011', '111011']
    graph = [list(map(int, line)) for line in input_data[1:]] # 뒤에 for문 부터 먼저 해석해야함
    # line : 각각의 반복에서 미로의 한 행을 나타내는 문자열. 
    # for 반복문에서의 line = '101111' (문자열)
    # list(map(int, line)) 수행 시 문자열에서 문자 하나하나를 int로 바꿔 list로 반환. '101111' -> [1, 0, 1, 1, 1, 1]


# 방법 3 : 리스트 내포와 input() 함수 사용 (코드가 간결하고 파이썬스럽게 작성되지만 리스트 내포를 처음 접하는 사람에겐 어려울 수 있음)
def inputGraph_listComprehension():
    N, M = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(N)] # 행 만큼 반복하여 입력받은 문자열의 각 문자를 int(정수)로 변환하여 리스트로 변환하여 반환 
    # 반복문을 한번 돌 때 graph에 [1, 0, 1, 1, 1, 1]가 추가됨. 두 번째 돌 땐 두 번째 행으로 [1, 0, 1, 0, 1, 0]가 추가됨