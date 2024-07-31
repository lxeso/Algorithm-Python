# 수열 백준 2559번
# 입력 : 첫째 줄에는 두개의 정수(N=온도를 측정한 전체 날짜의 수, K=합을 구하기 위한 연속적인 날짜의 수)가 한개의 공백을 사이에 두고 순서대로 주어짐. 
# 출력 : 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.
# 구간합

sN, sK = input().split()
N = int(sN)
K = int(sK)
temperature_list = [list(map(int, input().split()) for _ in range(N))]

sum = 0
max = -99999999999

for j in range((N)-(K)):
    for i in range(j, (K)):
        sum += int(temperature_list[i])
    if max < sum:
        max = sum

print(max)