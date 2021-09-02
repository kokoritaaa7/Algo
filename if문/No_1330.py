'''
백준 알고리즘
https://www.acmicpc.net/problem/1330
두 수 비교하기

2021.07.23
'''

def compare(num1, num2):
    '''두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램'''
    if num1 < num2 :
        return '<'
    elif num1 > num2 :
        return '>'
    else:
        return '=='

num1, num2 = tuple(map(int,input().split(' ')))
print(compare(num1, num2))

