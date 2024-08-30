# 백준 3474번 '교수가 된 현우'
# 문제 :  N!이 얼마나 큰지 대략적으로나마 알려주기 위해, 자연수 N이 주어지면 N!의 오른쪽 끝에 있는 0의 개수를 알려주는 코드 구현
# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어지고, 이어서 T개의 줄에 정수 N이 주어진다(1 <= N <= 1000000000).
# 출력 : 각 줄마다 N!의 오른쪽 끝에 있는 0의 개수를 출력한다.
# 문제 해결 핵심 포인트 : 0의 개수는 결국 x10이 몇번 반복되는지(곱해지는지)를 뜻하고, 10은 2X5로 이루어져 있는데, 팩토리얼(!)에선 무조건 5보다 2가 더 많이 곱해질 수 밖에 없기 때문에, 5가 몇번 곱해지느냐가 곧 0의 개수를 의미함.
# 그러므로 N!의 소인수분해 결과에서 5가 몇번 곱해지는지를 계산해서 출력하면 됨! 

def counting_zero(N):
    count = 0 # 0의 개수를 저장할 변수

    while N >= 5: # N이 5로 안나눠질때까지(5이상일때까지) 반복
        N //= 5 # N을 5로 나누어 5의 배수 개수를 셈
        count += N # 5의 배수의 개수를 count에 더함

    return count # 결과 반환

def solution():
    import sys
    input = sys.stdin.read # 한번의 모든 입력 받음
    data = input().split() # 입력을 공백 기준으로 나눠 리스트로 저장
    T = int(data[0])

    result = []

    for i in range(1, T + 1): # 각 테스트 케이스마다
        N = int(data[i]) # N을 입력받음
        result.append(str(counting_zero(N))) # 각 N마다 0의 개수 반복할때마다 추가
    sys.stdout.write("\n".join(result) + "\n") # 결과를 한 번에 줄 마다 출력


# 예제 실행
solution()


# 입력 처리 방법 1(틀림)
def solution():    
    T = int(input()) # 테스트 케이스 숫자 입력받기

    for _ in range(T): # 각 테스트 케이스마다 실행
        N = int(input()) # 숫자 입력 받기
        print(counting_zero(N)) # 함수 호출