'''
백준 알고리즘
https://www.acmicpc.net/problem/9498
시험 성적

2021.07.23
'''

def grade(score):
    '''시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램'''
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = int(input())
print(grade(score))