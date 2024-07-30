# 한국이 그리울 땐 서버에 접속하지 백준 9996번
# 입력 : 파일 개수 N(1<=N<=100), 패턴(알파벳 소문자+'*'(42)), N개의 줄에 파일 이름(알파벳 소문자로만 이루어짐)
# 출력 : 총 N개의 줄에 걸쳐, 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력
# 예시 : "abcd", "ad", "anestod" 는 전부 패턴 "a*d"와 일치
# 특이사항 : 패턴의 '*'의 경우, 문자열의 시작과 끝에 있지 않음. 패턴은 문자열의 시작!과 끝! 부분이 일치해야함

# 입력
N = int(input()) # 파일 개수
pattern = input().split('*')
file_names = [input() for _ in range (N)]

results = []

for file_name in file_names:
    if file_name.startswith(pattern[0]) and file_name.endswith(pattern[1]) and len(file_name) >= len(pattern[0]) + len(pattern[1]): # 만일 패턴 * 앞부분이 이름 안에 존재한다면, 해당 끝 인덱스를 문자열 slicing하고 다른 if문으로 패턴 * 뒷부분도 이름 안에 좋재하는지 확인
        results.append("DA")
    else:
        results.append("NE")

for result in results:
    print(result)