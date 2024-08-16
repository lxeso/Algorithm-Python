# 백준 1992번 쿼드 트리 (2차원 배열을 재귀적으로 분할)
# 쿼드 트리 : 주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다
# 입력 : 첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
# 출력 : 영상을 압축한 결과를 출력한다.

def solution(x, y, size):
    # 주어진 영역이 모두 같은 숫자인지 확인
    current = graph[x][y]
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != current:
                all_same = False
                break
        if not all_same:
            break
    
    # 모두 같은 숫자라면, 그 숫자를 반환
    if all_same:
        return current
    
    # 다른 숫자가 섞여있다면, 4분할하여 재귀적으로 처리
    half = size // 2
    top_left = solution(x, y, half)  # 왼쪽 위
    top_right = solution(x, y + half, half)  # 오른쪽 위
    bottom_left = solution(x + half, y, half)  # 왼쪽 아래
    bottom_right = solution(x + half, y + half, half)  # 오른쪽 아래
    
    # 네 개의 결과를 결합하여 반환
    return f'({top_left}{top_right}{bottom_left}{bottom_right})'

# 입력 처리
N = int(input())  # 영상의 크기
graph = [input().strip() for _ in range(N)]  # 영상의 각 줄을 입력받아 리스트로 저장

# 압축 결과 출력
result = solution(0, 0, N)
print(result)
