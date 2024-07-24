# 트럭 주차 
# 입력 : 요금 A, B, C / 트럭 도착시간(1~100), 떠난시간(1~100) (도착시간 < 떠난시간)
# 출력 : 트럭 주차 비용
# 트럭 1대 : 1분에 한 대당 A원, 트럭 2대 : 1분에 한 대당 B원, 트럭 3대 : 1분에 한 대당 C원
# 핵심 포인트 : 시간 배열 생성 후 트럭이 존재하는 시간마다 count +1로 올려줌
# 입력이 문제. 한 줄 입력이냐, 세 줄 입력이냐에 따라 주차하는 트럭 개수가 달라지는 것이므로 몇 줄 입력인지 세야 되는데 어떻게 세야될지 모름
# 아 잘 못 생각함.. 트럭 세대는 무조건 주차하는 것이고 트럭 주차 시간 겹침 여부에 따라 요금이 달라지는 것

# 1. 입력 받기
A, B, C = map(int, input().split()) # 요금 A, B, C를 각각의 변수에 입력 받음
truck_times = [list(map(int, input().split())) for _ in range(3)] # 그 다음 입력인 [트럭의 도착시간, 떠난시간] 세번 반복해서 받음

# 2. 시간 리스트 선언 및 초기화 후 시간대별 트럭 수 리스트에 추가
time_count = [0] * 101 # 시간 범위 1-100

for start, end in truck_times: # [트럭의 도착시간, 떠난시간] 기준 반복문 
    for x in range(start, end): # [도착시간, 떠난시간] 사이 시간들을 접근하는 반복문
        time_count[x] += 1 # 해당 사이 시간들의 count를 올려줌

# 3. 주차 요금 계산
result_cost = 0

for count in time_count:
    if count == 1: # 트럭 : 1대
        result_cost += A
    elif count == 2: # 트럭 : 2대
        result_cost += B*2 
    elif count == 3: # 트럭 : 3대
        result_cost += C*3

print(result_cost)