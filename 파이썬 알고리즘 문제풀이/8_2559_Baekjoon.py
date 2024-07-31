# 수열 백준 2559번
# 입력 : 첫째 줄에는 두개의 정수(N=온도를 측정한 전체 날짜의 수, K=합을 구하기 위한 연속적인 날짜의 수)가 한개의 공백을 사이에 두고 순서대로 주어짐. 
# 출력 : 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.
# 구간합

N, K = map(int, input().split())
temperature_list = list(map(int, input().split()))

current_sum = sum(temperature_list[:K])
max_sum = current_sum

for i in range(K, N): # i = 2,3,4 , K= 2, N = 10 현재값 + 바로 전 인덱스 값 + 바로 후 인덱스 값 temperature_list[]
    current_sum = current_sum - temperature_list[i-K] + temperature_list[i]
    if max_sum < current_sum:
        max_sum = current_sum
print(max_sum)