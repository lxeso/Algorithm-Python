# 백준 10815번 숫자 카드 - 이진탐색
# 문제 : 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다


'''
이진 탐색 이용
1. 상근이가 가지고 있는 숫자 카드의 수 N 입력받음
2. 상근이가 가지고 있는 숫자 카드의 개수 N만큼 숫자 카드를 list(map(int, input().split())) 으로 입력받음
3. 목표 카드들의 개수 M을 입력받음 int(input())
4. 목표 카드들을 리스트로 공백으로 분리시켜서 입력받음 list(map(int, input().split()))
5. 숫자 카드들을 정렬
6. 이진 탐색을 시전함. low = 0, high = N - 1 하고, while low <= high 반복문 돌리고 목표카드와 일치하는게 있으면 1을 answer_list에 추가, 없었다면 0을 anwser_list에 추가 후 마지막에 리스트 출력 시킴

'''

N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

card_list.sort()




def binary_search(target_num):
    low = 0
    high = N - 1
    flag = False
    while low <= high:
        mid = (low + high) // 2
        if card_list[mid] > target_num:
            high = mid - 1
        elif card_list[mid] < target_num:
            low = mid + 1
        else: # card_list[mid] == target_num
            return 1
    
    return 0

answer_list = [binary_search(target_num) for target_num in target_list]

print(" ".join(map(str, answer_list)))