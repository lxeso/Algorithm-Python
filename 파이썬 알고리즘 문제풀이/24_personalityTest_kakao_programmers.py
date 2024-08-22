# 프로그래머스 카카오 '성격 유형 검사하기' 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 문제 : 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어집니다. 
# 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.


def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0, 
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    for i in range(len(survey)):
        choice = choices[i]
        if choice < 4: # 비동의
            scores[survey[i][0]] += 4 - choice
        elif choice > 4: # 동의
            scores[survey[i][1]] += choice - 4
        
        result = ''
        result += 'R' if scores['R'] >= scores['T'] else 'T'
        result += 'C' if scores['C'] >= scores['F'] else 'F'
        result += 'J' if scores['J'] >= scores['M'] else 'M'
        result += 'A' if scores['A'] >= scores['N'] else 'N'
    return result

# 입력 처리
survey_input = input()  # 첫 번째 입력: ["AN", "CF", "MJ", "RT", "NA"]
choices_input = input()  # 두 번째 입력: [5, 3, 2, 7, 5]

# 입력된 문자열을 리스트로 변환하기
# survey_input: '["AN", "CF", "MJ", "RT", "NA"]' 를 실제 리스트로 변환
survey = survey_input.strip('[]').replace('"', '').split(', ')
# choices_input: '[5, 3, 2, 7, 5]' 를 실제 리스트로 변환
choices = list(map(int, choices_input.strip('[]').split(', ')))

print(solution(survey, choices))