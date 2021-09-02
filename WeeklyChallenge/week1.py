'''
프로그래머스 위클리 챌린지
https://programmers.co.kr/learn/courses/30/lessons/82612
1주차

2021.08.21
'''

'''
문제 이해하기
놀이 기구 이용료 : price
놀이 기구 이용 횟수에 따라 price * n

갖고 있는 돈에서, cnt만큼 탈 때 모자란 돈 계산하기
금액 부족하지 않으면 0 출력
'''


def solution(price, money, count):
    total_m = 0
    for cnt in range(1, count+1):
        total_m += price * cnt

    if total_m > money:
        return total_m - money

    return 0

print(solution(3, 20, 4))

def solution2(price, money, count):
    total_m = price * (count * (count+1)) // 2
    return total_m - money if total_m > money else 0

print(solution2(3, 20, 4))