# 백준 1654번 랜선 자르기
'''
길이가 제각각인 K개의 랜선을 잘라 모두 N개의 같은 길이의 랜선으로 만들고 싶은 상태. N개보다 많이 만드는 것도 N개를 만드는 것에 포함됨.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오
[입력]
첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. 항상 N은 K 이하이다.
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다
[출력]
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
'''

'''
<알고리즘>
1. 이미 가지고 있는 랜선의 개수 K와 필요한 랜선의 개수 N을 입력받음
2. 랜선의 길이를 int로 리스트 안에 for 반목문으로 K번 만큼 입력받음
3. 구해야 하는 랜선의 최대 길이를 H라 한다면, H가 가질 수 있는 최소값은 0(N = K이고 주어진 랜선길이가 모두 같을때)이지만, total_num_of_lan을 구하는 과정에서 나누기 연산을 사용하기 때문에 H는 절대 0이 되면 안되므로 low는 1로 설정해야하고,  최댓값은 가진 랜선 길이들 중 최소값 min(lan_list)가 됨.
4. H값을 이진탐색으로 구함
5. H값이 주어졌을때, 몇개의 같은 길이를 가진 랜턴을 만들 수 있는지 계산해야함
5-1. total_num_of_lan += lan_list[i] // H
5-2. 이제 total_num_of_lan와 M값을 비교해서 total_num_of_lan >= M 이라면, 계속 오른쪽을 더 탐색해서 최대가 되는 H값을 answer에 저장시킨 후 반복문 종료 후 반환.
'''


def binary_search(lan_list, M):
    low = 0
    high = max(lan_list)
    answer = 0

    while low <= high:
        total_num_of_lan = 0
        mid = (low + high) // 2
        for lan in lan_list:
            total_num_of_lan += lan // mid

        if total_num_of_lan < M: # 필요한 랜턴의 개수보다 작다면 H를 줄여야함
            high = mid - 1
        else: # total_num_of_lan >= M 인 경우,
            answer = mid # 우선 정답 저장 후
            low = mid + 1 # 오른쪽 더 탐색
    return answer

K, M = map(int, input().strip().split())
lan_list = [ int(input().strip()) for _ in range(K)]
print(binary_search(lan_list, M))