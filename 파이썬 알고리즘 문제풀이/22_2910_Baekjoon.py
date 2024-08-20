# 벡준 2910번 '빈도 정렬' (정렬 알고리즘)
# 문제 : 메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 창영이는 이 숫자를 자주 등장하는 빈도순대로 정렬하려고 한다. 
# 만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다. 이렇게 정렬하는 방법을 빈도 정렬이라고 한다.
# 수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 메시지의 길이 N과 C가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ C ≤ 1,000,000,000) 둘째 줄에 메시지 수열이 주어진다.
# 출력 : 첫째 줄에 입력으로 주어진 수열을 빈도 정렬한 다음 출력한다.
from collections import Counter

def solution(N, C, array):
    frequency = Counter(array) # 각 숫자의 빈도를 ㄱ몌산

    sorted_array = sorted(array, key=lambda x: (-frequency[x], array.index(x))) # key에 따라 정렬을 수행 #첫번째 기준 (-frequency[x]): 빈도가 높은 순서대로 (빈도는 음수로 뒤집어 정렬 #두번째 기준(sequence.index(x)): 빈도가 같은 경우, 처음 등장한 순서대로 정렬

    return sorted_array

N, C = map(int, input().split())
array = list(map(int,input().split()))
sorted_array = solution(N, C, array)
print(' '.join(map(str, sorted_array)))