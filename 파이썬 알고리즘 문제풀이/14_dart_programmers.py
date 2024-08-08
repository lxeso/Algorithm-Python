# 다트 게임 프로그래머스
def solution(dartResult):
    scores = []
    n = len(dartResult)
    i = 0
    
    while i < n:
        if dartResult[i+1].isdigit(): # 점수가 10인 경우
            score = 10
            i += 1
        else: # 점수가 0-9인 경우
            score = int(dartResult[i])
        
        i += 1
        
        if dartResult[i] == 'S':
            score **= 1
        elif dartResult[i] == 'D':
            score **= 2
        elif dartResult[i] == 'T':
            score **= 3
            
        i += 1
        
        if i < n and dartResult[i] == '*':
            if scores:
                scores[-1] *= 2
            score *= 2
            i += 1
        elif i < n and dartResult[i] == '#':
            score *= -1
            i += 1
        scores.append(score)
    
    return sum(scores)