# 9375번 백준 패션왕 신해빈
# 해빈이는 한 번 입었던 옷들의 조합을 절대 다시 입지 않음. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
# 입력 : 
# 첫째 줄에 테스트 케이스(최대 100개)가 주어짐. 각 테스트케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(1<=n<=30)이 주어진다. 
# 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있음. (모든 문자열은 1이상 20이하의 알파벳 소문자. 이름 중복 X)
# 출력 : 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 입을 수 있는 경우를 출력하시오.
# 수열 조합 알고리즘?
#def solution():
def solution(test_cases):
    results = []

    for case in test_cases: # 첫 번째 테스트 케이스: (3, [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']])
        clothes = case[1]  # 첫 번째 루프에서는 clothes = [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]
        category_dict = {}

        for cloth, category in clothes:
            if category in category_dict:
                category_dict[category].append(cloth)
            else:
                category_dict[category] = [cloth]
        # 첫 번째 루프 후 category_dict = {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}

        combinations = 1
        for category in category_dict:
            combinations *= (len(category_dict[category]) + 1) # headgear: 2+1, eyewear: 1+1 => 3 * 2 = 6

            # 첫 번째 케이스에서는
            # 'headgear' 카테고리: 2개의 아이템 (hat, turban) -> (2 + 1)
            # combinations = 1 * 3 = 3
            # 'eyewear' 카테고리: 1개의 아이템 (sunglasses) -> (1 + 1)
            # combinations = 3 * 2 = 6
        results.append(combinations - 1)  # 첫 번째 결과는 6 - 1 = 5

        # 두 번째 루프에서는 clothes = [['mask', 'face'], ['sunglasses', 'face'], ['makeup', 'face']]
        # 두 번째 루프 후 category_dict = {'face': ['mask', 'sunglasses', 'makeup']}
        # 두 번째 결과는 (3 + 1) - 1 = 3

    return results # 결과는 [5, 3]

# 입력 처리 부분
test_cases = [] # 튜플 : 조회만 가능
num_cases = int(input()) # num_cases = 2

for _ in range(num_cases):
    n = int(input()) # 첫 번째 루프에서는 n = 3
    clothes = [input().split() for _ in range(n)]  # 첫 번째 루프(테스트케이스)에서는 clothes = [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]
    test_cases.append((n, clothes))  # 첫 번째 루프 이후 test_cases = [(3, [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']])] # 두 번째 루프 이후 test_cases = [(3, [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]), (3, [['mask', 'face'], ['sunglasses', 'face'], ['makeup', 'face']])]

# 결과 계산 및 출력
results = solution(test_cases)
for result in results:
    print(result)
