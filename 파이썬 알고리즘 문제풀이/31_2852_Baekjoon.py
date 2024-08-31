# 백준 2852번 'NBA 농구'
# 48분 동안 진행되는 농구 경기에, 동혁이는 골이 들어갈 때 마다 골이 들어간 시간과 팀을 적는 이상한 취미를 가지고 있다. 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 골이 들어간 횟수 N(1<=N<=100)이 주어진다. 둘째 줄부터 N개의 줄에 득점 정보가 주어진다. 득점 정보는 득점한 팀의 번호와 득점한 시간으로 이루어져 있다. 팀 번호는 1 또는 2이다. 
# 득점한 시간은 MM:SS(분:초) 형식이며, 분과 초가 한자리 일 경우 첫째자리가 0이다. 분은 0보다 크거나 같고, 47보다 작거나 같으며, 초는 0보다 크거나 같고, 59보다 작거나 같다. 득점 시간이 겹치는 경우는 없다.
# 출력
# 첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간을 출력한다. 시간은 입력과 같은 형식(MM:SS)으로 출력한다.

def time_to_seconds(time): # MM:SS 형식을 초 단위로 변환
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds

def seconds_to_time(seconds): # 초를 MM:SS 단위로 변환
    minutes = seconds // 60 # 초를 60으로 나눈 몫
    seconds = seconds % 60 # 초를 60으로 나눈 나머지
    return str(minutes).zfill(2) + ":" + str(seconds).zfill(2) # zfill은 문자열이 특정 길이에 도달할 때까지 왼쪽을 0으로 채우는 메서드


def solution():
    N = int(input()) # 득점 횟수 N
    scores = [] # 각 득점 기록을 저장할 리스트

    for _ in range(N):
        team, time = input().split() # 팀 번호화 득점 시간을 입력 받음
        team = int(team) # 정수형으로 변환
        time_in_seconds = time_to_seconds(time) # 시간을 초 단위로 변환
        scores.append((team, time_in_seconds)) # (팀 번호, 초 단위 시간)을 튜플로 저장

    team1_winning_time = 0 # 1번 팀이 이기고 있던 시간
    team2_winning_time = 0 # 2번 팀이 이기고 있던 시간
    last_goal_time = 0 # 마지막으로 득점이 발생한 시간
    team1_score = 0 # 1번 팀의 득점
    team2_score = 0 # 2번 팀의 득점

    for team, current_goal_time in scores:
        if team1_score > team2_score: # 1번 팀 이기고 있을 때
            team1_winning_time += current_goal_time - last_goal_time # 현재 1번팀이 이기고 있다면, 마지막 득점 시간에서 현재 득점 시간 차이 계산해서 더함
        if team2_score > team1_score: # 2번 팀 이기고 있을 때
            team2_winning_time += current_goal_time - last_goal_time # 위와 같음

        # 득점에 따라 점수 갱신
        if team == 1:
            team1_score += 1
        elif team ==2:
            team2_score += 1
        
        # 현재 시간 갱신
        last_goal_time = current_goal_time

    # 경기 종료 시점까지 이기고 있는 시간 추가 계산
    end_time = time_to_seconds("48:00")
    if team1_score > team2_score:
        team1_winning_time += end_time - last_goal_time
    elif team2_score > team1_score:
        team2_winning_time += end_time - last_goal_time
    
    print(seconds_to_time(team1_winning_time))
    print(seconds_to_time(team2_winning_time))

#예제 호출
solution()