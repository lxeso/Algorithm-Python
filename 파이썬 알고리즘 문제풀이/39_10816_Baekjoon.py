# 백준 10816번 숫자카드 2 - 이진 탐색
# 문제 조건 : 상근이가 가지고 있는 N개의 숫자 카드 중 안에 정수 M개가 각각 몇번 포함되어있는지에 대한 카운트를 출력해라

'''
알고리즘
1. 숫자카드의 개수 N을 int(input())으로 입력받음
2. 숫자카드에 적혀있는 정수들을 num_list에 list(map(int, input().split()))으로 입력받음
3. 상근이가 몇개 가지고 있는 숫자카드인지 구해야 할 M개의 정수에서 M을 int(input())으로 입력받음 
4. M개의 정수를 target_list에 list(map(int, input().split())) 으로 입력받음.
5. N개의 정수들을 sort() 함수로 정렬 후, 이진 탐색을 시작함
6. low와 high를 지정하고, 이에 따라 mid를 지정함.
7. num_list[mid]와 target_list의 target_num 숫자들과 비교함. 
7-1. num_list[mid]가 target_num보다 크다면 high = mid - 1 로 설정
7-2. num_list[mid]가 target_num보다 작다면, low = mid + 1 로 설정
7-3. num_list[mid]가 target_num과 같다면, count + 1 해주고, 계속 반복문 돌림?  num_list[mid] == target_num 일치했을 때 low나 high를 변경 시켜야함. 어떻게? 정렬되어 있으니까.. low를 mid + 1로 설정?
7-4. 반복문의 조건은 동일해도 됨. 반복문 다 돌고 count를 반환.
8. 반환받은 count들의 하나의 리스트에 저장시킨 후 print(" ".join(map(str, answer_list))) 로 출력
'''

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))
num_list.sort()


def binary_search(target_num):
    low = 0
    high = N - 1
    start_index = -1
    end_index = -1

    # 타켓 넘버의 시작 인덱스 찾기
    while low <= high:
        mid = (low + high) // 2
        if num_list[mid] > target_num:
            high = mid - 1
        elif num_list[mid] < target_num:
            low = mid + 1
        else: # 왼쪽을 더 탐색
            high = mid -1
            start_index = mid

    low = 0
    high = N - 1
    # 타켓 넘버의 끝 인덱스 찾기
    while low <= high:
        mid = (low + high) // 2
        if num_list[mid] > target_num:
            high = mid - 1
        elif num_list[mid] < target_num:
            low = mid + 1
        else: 
            low = mid + 1
            end_index = mid

    if start_index == -1 or end_index == -1:
        return 0
    
    count = end_index - start_index + 1

    return count

answer_list = [binary_search(target_num) for target_num in target_list]

print(" ".join(map(str, answer_list)))