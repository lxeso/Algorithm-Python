# 백준 10709번 '기상 캐스터'
'''
#문제
JOI시는 남북방향이 H 킬로미터, 동서방향이 W 킬로미터인 직사각형 모양이다. JOI시는 가로와 세로의 길이가 1킬로미터인 H × W 개의 작은 구역들로 나뉘어 있다. 북쪽으로부터 i 번째, 서쪽으로부터 j 번째에 있는 구역을 (i, j) 로 표시한다.
각 구역의 하늘에는 구름이 있을 수도, 없을 수도 있다. 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다. 오늘은 날씨가 정말 좋기 때문에 JOI시의 외부에서 구름이 이동해 오는 경우는 없다.
지금 각 구역의 하늘에 구름이 있는지 없는지를 알고 있다. 기상청에서 일하고 있는 여러분은 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 일을 맡았다.
각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.

#입력
입력은 1 + H 행으로 주어진다.
첫 번째 행에는 정수 H, W (1 ≦ H ≦ 100, 1 ≦ W ≦ 100) 가 공백을 사이에 주고 주어진다. 이것은 JOI시가 H × W 개의 작은 구역으로 나뉘어 있다는 것을 의미한다.
이어진 H 개의 행의 i번째 행 (1 ≦ i ≦ H) 에는 W문자의 문자열이 주어진다. W 개의 문자 중 j번째 문자 (1 ≦ j ≦ W) 는, 구역 (i, j) 에 지금 구름이 떠 있는지 아닌지를 나타낸다. 구름이 있는 경우에는 영어 소문자 'c' 가, 구름이 없는 경우에는 문자 '.' 가 주어진다.

#출력
출력은 H 행으로, 각 행에는 공백으로 구분된 W 개의 정수를 출력한다. 출력의 i 번째 행 j 번째 정수 (1 ≦ i ≦ H, 1 ≦ j ≦ W) 는, 지금부터 몇 분후에 처음으로 구역 (i, j) 에 구름이 뜨는지를 표시한다. 단, 처음부터 구역 (i, j) 에 구름이 떠 있었던 경우에는 0을, 몇 분이 지나도 구름이 뜨지 않을 경우에는 -1을 출력한다.
'''
# 주어진 도시의 구역에서 구름이 어디에 있고, 몇 분 후에 각 구역에 구름이 도착할지 계산하는 문제
# 각 구역에 대해 구름이 몇 분 후에 도착하는지를 계산하여 출력
# 필요한 알고리즘 및 지식 : 2차원 배열의 순차적 탐색'=
# 접근 방식 : 각 구역을 순차적으로 검사하면서, 구름이 있는 위치를 발견하면 그 위치부터 오른쪽으로 구름이 언제 도착하는지를 계산해 나가면 됨. 만약 구름이 없거나 구름이 도착하지 않는 구역은 '-1'로 표시

def solution():
    # 입력 처리 및 초기 변수 설정
    H, W = map(int, input().split()) # H: 행의 개수, W: 열의 개수
    city = [input() for _ in range(H)] # 도시의 구역 정보를 2차원 리스트로 입력 받음

    # 결과를 저장할 리스트 초기화, 초기값은 모두 -1로 설정
    result = [[-1] * W for _ in range(H)]

    # 구역을 순차적으로 탐색하며 구름의 위치와 시간을 계산
    for i in range(H): # 각 행을 탐색
        time = -1 # 현재까지 구름이 도착하는 데 걸리는 시간을 기록하는 변수, 초기값은 -1
        for j in range(W): # 각 열을 탐색
            if city[i][j] == 'c': #현재 위치에 구름이 있다면
                time = 0 # 현재 위치에 구름이 도착했으므로 시간을 0으로 설정
                result[i][j] = time # 결과 리스트에 0을 기록
            elif time != -1: # 이전에 구름을 발견한 적이 있는가? -> 이 조건이 만족되면 현재 위치까지 구름이 도착할 수 있음을 의미
                time += 1 # 구름이 오른쪽으로 이동했으므로, 시간을 1 증가시킴
                result[i][j] = time # 현재 위치에 구름이 도착하는 시간을 기록
    # 결과 출력
    for i in range(H): # 행마다 반복
        print(" ".join(map(str, result[i]))) # 각 행의 결과를 출력

solution()