'''
백준 알고리즘
https://www.acmicpc.net/problem/2753
윤년

2021.07.23
'''

def isLeapYear(year):
    '''연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램'''
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return 1
    else:
        return 0

year = int(input())
print(isLeapYear(year))