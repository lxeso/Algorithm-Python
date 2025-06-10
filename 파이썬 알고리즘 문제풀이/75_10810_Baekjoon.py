# 백준 10810번 공 넣기

import sys
input = sys.stdin.readline

def ball_10810():
    N, M = map(int, input().strip().split(' '))
    baskets = {}
    for x in range(1, N+1):
        baskets[x] = 0
    # baskets = {1:0, 2:0, 3:0, 4:0, ... , N:0}
    for _ in range(M):
        i, j, k = map(int, input().strip().split(' '))
        for y in range(i, j+1):
            baskets[y] = k
    for z in range(1, N+1):
        print(baskets[z], end=" ")

def ball_10813():
    N, M = map(int, input().strip().split(' '))
    baskets = [0] * (N+1)
    for x in range(1, N+1):
        baskets[x] = x # baskets = [1, 2, 3, 4, 5, 6, ..., N]
    for y in range(1, M+1):
        i, j = map(int, input().strip().split(' '))
        temp = baskets[i]
        baskets[i] = baskets[j]
        baskets[j] = temp
    for z in range(1, N+1):
        print(baskets[z], end = " ")

def ball_10811():
    N, M = map(int, input().strip().split(' '))
    baskets = list(range(1, N+1)) # baskets = [0, 1, 2, 3, ..., N]
    for _ in range(M):
        i, j = map(int, input().strip().split(' ')) # i=4, j=7
        baskets[i-1:j] = baskets[i-1:j][::-1]
    print(*baskets)

def clock_2884(): # 현재 시간에서 45분 전 시간 출력
    H, M = map(int, input().strip().split(' '))
    # 1. 분(M)이 45 이상일때
    # 1. 분(M)이 45 미만일때
    if (M >= 45):
        M = M - 45
    else: # M이 45분 미만일때
        if(H == 0): # 0시일때만 23으로 바꿔줌
            H = 23
            M = 60 + M -45
        else:
            H = H-1
            M = 60 + M - 45
    print(H, M)

def clock_2525(): # 입력된 A시B분에 C분을 더한 시간 출력
    A, B = map(int, input().strip().split(' '))
    C = int(input())
    # C를 60으로 나눈 몫(chour)과 나머지(cminute)로 시간과 분을 구함
    # result_hour = A+chour : 24 이상이라면 24로 나눈 나머지로 설정
    # result_minute = B+cminute : 60 넘어가면 result_hour+1 해줌 (120을 넘어갈 순 없음)
    chour = C // 60
    cminute = C % 60
    result_hour = 0
    result_minute = 0
    if (B+cminute >= 60):
        result_hour += 1
        result_minute = B + cminute - 60
    else: # B+cminute < 60
        result_minute = B + cminute
    
    result_hour = result_hour + A + chour
    if (result_hour>23):
        result_hour = result_hour % 24
    print(result_hour, result_minute)

def dice_2480(): # 주사위 숫자 3개 중 같은 숫자 개수에 따라 상금이 달라지는데, 상금을 계산해 출력하는 문제
    a, b, c = map(int, input().strip().split(' ')) # 주사위 3개
    dice_list = [a, b, c]
    # 같고 다름을 어떻게 비교하지..?
    # 1. 3개 모두 같을 때 (a == b == c)
    # 2. 2개만 같을때 (3개 다 같을 경우는 위의 조건문에 들어가므로 2개만 비교 가능. a==b, b==c, a==c)
    # 3. 나머지 (자동으로 모두 다를 경우)
    result = 0
    if a==b==c:
        result = 10000 + (a*1000)
    elif (a==b):
        result = 1000 + (a*100)
    elif (b==c):
        result = 1000 + (b*100)
    elif (a==c):
        result = 1000 + (a*100)
    else:
        result = (max(dice_list))*100
    print(result)


def tienum_1744():
    N = int(input()) # n = 6
    numbers = [int(input()) for _ in range(N)] # numbers = [0, 1, 2, 3, 4, 5]

    plus = [] # 양수
    minus = [] # 음수
    ones = 0 # 1

    for num in numbers: # 수 분류시킴
        if num > 1:
            plus.append(num)
        elif num == 1:
            ones += 1
        else:
            minus.append(num)
        
        # plus = [2, 4, 3, 5] → 모두 양수 중 2 이상
        # ones = 1 → 1은 따로 더함
        # minus = [0] → 0이나 음수는 묶어야 이득
    
    # 양수는 앞에서부터 큰 수끼리 곱하기 쉽게 내림차순 정렬 
    plus.sort(reverse=True) # plus = [5, 4, 3, 2]

    # 음수는 작은 수 끼리
    minus.sort() 

    result = 0

    for i in range(0, len(plus)-1, 2): # 묶은 수 또 묶이면 안되므로 2씩 증가시키며 반복문 실행
        result += plus[i]*plus[i+1]
    
    if len(plus) % 2 == 1: # 홀수개면 2개씩 묶이다가 나머지 1개는 남으므로 그냥 따로 더해줌
        result += plus[-1] #마지막 수 = 마지막 인덱스 = -1
    
    for i in range(0, len(minus)-1, 2): # 음수도 오름차순 정렬시킨 상태에서 2개씩 묶어서 곱한다음에 result에 더함 minust = [-5, -4, -3, -2, 0]
        result += minus[i]*minus[i+1]
    
    if len(minus) % 2 == 1: # 음수도 홀수개면 마지막 한개 남으므로 따로 더해줌. 여기서 0도 자동으로 처리됨
        result += minus[-1]

    result += ones # 1은 무조건 더하는게 이득이므로 마지막으로 따로 더해줌(1은 곱해도 똑같으니까 곱하는 의미가 없음)

    print(result)
    '''
    - 어떻게 묶어야 최대가 될지 수의 특성에 따라 분류함
        - 양수는 무조건 큰수끼리 묶어야 이득
        - 음수는 절댓값이 큰 음수끼리 묶어야 이득
        - 1은 곱하는 의미가 없으므로 묶지 않고 따로 더해주는게 이득
        - 0은 남은 음수랑 곱해지거나 더해지는게 이득.
    - 그래서 수열을 각각 양수, 음수(0포함), 1 로 분류를 함
    - 수열 안 숫자들 돌면서 분류시킴
    - 양수는 내림차순으로 정렬(반복문 순서 생각) plus = [5, 4, 3, 2, 1]
    - 음수는 오름차순으로 정렬 (절댓값으로 생각) minus = [-5, -4, -3, -2, -1]
    - 양수와 음수 둘다 각각 for반복문으로 2칸씩 띄어서 돌며(같은 수는 또 묶이면 안되므로) 2개씩 묶어서 곱하고 result에 더해주고, 개수가 홀수일경우 마지막 남은 숫자 1개는 따로 더해줌
    - 마지막으로 1은 따로 나온 개수만큼 더해줌
    '''

def triangle_programmers(triangle): # 아래에서부터 위로 올라가면서 계산
    dp = [row[:] for row in triangle] # [:] : 슬라이싱으로, 전체를 자른다는 것 -> 전체 복사를 의미 (슬라이싱은 리스트의 일부 요소를 잘라 새로운 리스트로 만드는 것)
    # dp = triangle 로 안하는 이유는 이렇게 하면 얕은 복사로 둘이 아예 같은 리스트를 가리키게 됨
    '''
    즉, triangle의 각 row(리스트)를 하나씩 꺼내서 row[:]를 써서 복사하고 그 복사본들을 [ ... ]로 묶어서 새 리스트를 만든다는 뜻!

        triangle = [
            [7],
            [3, 8],
            [8, 1, 0]
        ]
    '''

    for i in range(len(dp)-2, -1, -1): # 마지막줄 바로 윗줄(len(dp)-2)부터 시작해 1씩 줄어들면서 0까지 반복 (-1인 이유는 끝 인덱스는 포함 안하기 때문)
        for j in range(len(dp[i])): # 칸 개수
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
        
    return dp[0][0] # dp[i][j]는 i번째 줄의 j번째 숫자까지 도달했을 때의 최대 누적합이므로 [0][0]부터 시작한 누적합 출력

def hatesamenum_programmers(arr):
    answer = []
    for num in arr:
        #answer가 비어있거나, 마지막에 넣은 값과 다르다면 추가
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer

def string_9086():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        word = input().strip()
        print(word[0] + word[-1])

def string_10809():
    result = [-1]*26 # 내가 원하는 result = [-1, -1, -1, ..., -1] -1이 26개
    S = list(input().strip()) # 알파벳 소문자로만 이루어져 있음
    for i in range(len(S)):
        # 이중 for문..? ord 사용? 알파벳 개수 26개 <- 너무 어렵게 생각한 것.. 
        # 등장하는 첫위치.. 
        index = ord(S[i]) - ord('a') # 이걸로 바로 index 구할 수 있음
        if result[index] == -1: # 아직 등장하지 않았을 경우에만 바꿔줌
            result[index] = i
    print(' '.join(map(str, result)))

def string_1152():
    import sys
    input = sys.stdin.readline
    sentences = list(input().strip().split())
    print(len(sentences))
def problem_27323():
    A = int(input())
    B = int(input())
    print(A*B)