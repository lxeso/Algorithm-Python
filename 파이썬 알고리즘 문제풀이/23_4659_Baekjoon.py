# 백준 4659번 비밀번호 발음하기
# 문제 : 패스워드 생성기를 테스트 해보고 품질 평가. 품질 기준은 아래와 같다
# 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다. 
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다. 
# 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
# 입력 : 입력은 여러개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다. 마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.
# 출력 : 각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라. (예제 출력 : <a> is acceptable. / <tv> is not acceptable.)


def is_acceptable(password):  
    vowels = {'a', 'e', 'i', 'o', 'u'}  # 모음을 나타내는 집합. 모음은 반드시 하나 이상 포함되어야 함.
    has_vowel = False  # 모음 포함 여부를 추적하는 변수. 처음에는 모음을 찾지 못했으므로 False로 설정.
    consecutive_vowels = 0  # 연속된 모음의 개수를 세기 위한 변수. 초기값은 0.
    consecutive_consonants = 0  # 연속된 자음의 개수를 세기 위한 변수. 초기값은 0.
    prev_char = ''  # 이전 문자와 현재 문자를 비교하기 위한 변수. 초기값은 빈 문자열.

    for i, char in enumerate(password):  # password 문자열을 한 문자씩 순회. i는 문자의 인덱스, char는 현재 문자를 의미. + # enumerate 함수 : 각 요소에 대해 인덱스와 값을 동시에 반환함. 형태는 (인덱스, 값)
        # 현재 문자가 모음인지 확인
        if char in vowels:  # 만약 현재 문자가 모음 집합에 포함되어 있다면
            has_vowel = True  # 모음이 하나라도 포함된 것으로 간주하여 has_vowel을 True로 설정.
            consecutive_vowels += 1  # 연속된 모음의 개수를 1 증가시킴.
            consecutive_consonants = 0  # 자음이 끊겼으므로 연속된 자음의 개수를 0으로 초기화.
        else:  # 현재 문자가 모음이 아니라면 (즉, 자음이라면)
            consecutive_vowels = 0  # 모음이 끊겼으므로 연속된 모음의 개수를 0으로 초기화.
            consecutive_consonants += 1  # 연속된 자음의 개수를 1 증가시킴.

        # 3개 이상의 모음 또는 자음이 연속되었는지 확인
        if consecutive_vowels >= 3 or consecutive_consonants >= 3:  
            # 연속된 모음 또는 자음이 3개 이상이면 즉시 False를 반환하고 함수 종료.
            return False

        # 같은 글자가 연속적으로 두 번 오는지 확인하되, 'ee'와 'oo'는 허용
        if prev_char == char and char not in {'e', 'o'}:  
            # 이전 문자와 현재 문자가 동일하고, 그 문자가 'e'나 'o'가 아니라면
            return False  # False를 반환하고 함수 종료.

        prev_char = char  # 이전 문자를 현재 문자로 업데이트하여 다음 반복에서 비교할 준비를 함.

    # 반복문을 모두 돌고 난 후, 모음이 하나도 포함되지 않았다면
    if not has_vowel:  
        return False  # False를 반환하고 함수 종료.

    return True  # 모든 조건을 만족하면 True를 반환하여 비밀번호가 "acceptable"하다고 판단함.

def solution():
    while True:
        password = input().strip()
        if password == 'end':
            break
        
        if is_acceptable(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")

# 예제 실행
solution()