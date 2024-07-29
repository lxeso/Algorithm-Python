# ROT13 백준 11655번
# 영어 알파벳을 13글자씩 밀어서 만드는 암호화의 일종 (대문자와 소문자에만 적용, 알파벳이 아니라면 원래 글자 그대로 남아 있어야 함)

def rot13(s):
    result = []

    for char in s:
        if 'a' <= char <= 'z': # 소문자인 경우
            new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z': # 대문자인 경우
            new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

word = input()

print(rot13(word))