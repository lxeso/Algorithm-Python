#프로그래머스 > 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기

# 입력 : 번호가 담긴 배열 numbers[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 왼손잡이인지 오른손잡이인지 알려주는 hand("left", "right")

# 출력 : 각 번호를 누른 엄지손가락이 왼손인지 오른손인지를 나타내는 연속된 문자열 result("LRLLLRLLRRL") 리턴 

def distance_between_two(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1]-point2[1])
    return distance

def solution(numbers, hand):
    result = []
    keypad_dic = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left_thumb = '*'
    right_thumb = '#'

    for number in numbers:
        if number in [1, 4, 7]: #왼쪽
            result.append('L')
            left_thumb = number
        elif number in [3, 6, 9]: #오른쪽
            result.append('R')
            right_thumb = number
        else:
            left_distance = distance_between_two(keypad_dic[left_thumb], keypad_dic[number])
            right_distance = distance_between_two(keypad_dic[right_thumb], keypad_dic[number])
            if left_distance > right_distance:
                result.append('R')
                right_thumb = number
            elif left_distance < right_distance:
                result.append('L')
                left_thumb = number
            else:
                if hand == 'right':
                    result.append('R')
                    right_thumb = number
                else:
                    result.append('L')
                    left_thumb = number

    return ''.join(result)

