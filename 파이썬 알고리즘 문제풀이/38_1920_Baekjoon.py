# 백준 1920 수 찾기 - 이진탐색
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

'''
이진 탐색
1. N을 int(input())으로 입력 받음
2. N개의 정수를 list(map(int, input().split()))로 리스트 형태로 입력받음
3. M을 int(input())으로 입력받음
4. M개의 정수를 list(map(int, input().split()))로 리스트 형태로 입력 받음
5. 이진탐색으로 low와 high를 설정하고 mid와 비교하여 그에 따라 low나 high를 재조정하고 다시 비교
5-1. 좀 더 자세히.. 말해보자면 high가 low보다 같거나 클 동안 반복문을 진행시키고, 반복문 안에서 target_num 값과 비교해서 만약 찾았으면 return 1 하고, 찾지 못했으면 return 0.
5-2. 같지 않았다면 크기 비교해서 low나 high를 재조정시킴
5-3. 주의할점 : mid값은 반복문 안에 적어줘야 한다. low와 high값에 따라 계속 계산되어야하기 때문에. 그리고 출력문 join 쓰는 방법도 주의해서 볼 것.
6. M개의 줄에 걸쳐 존재하면 1을, 존재하지 않으면 0을 출력시킴 print("\n".join(map(str, answer_list)))
'''
N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

num_list.sort()

def binary_search(target_num):
    low = 0
    high = N - 1
    
    while low <= high:
        mid = (low + high) // 2 # /가 아닌 // 사용
        if target_num < num_list[mid]:
            high = mid -1
        elif target_num > num_list[mid]:
            low = mid + 1
        else: # target_num == num_list[mid]
            return 1
    return 0

answer_list = [binary_search(target) for target in target_list]

print("\n".join(map(str, answer_list)))