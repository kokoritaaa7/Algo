'''
프로그래머스 - 스택/큐
https://programmers.co.kr/learn/courses/30/lessons/42584
주식가격

2021.09.28
'''

'''
문제 이해하기
prices에 있는 배열을 순서대로 하나씩 빼면서 남아있는 배열과 비교하기
작지 않으면 +1 작으면 break?
'''

### 효율성 실패 -> 시간초과
# enumerate()는 반복 자료형 내 원소를 하나씩 다 봐야하니까 O(n)
# range()는 O(1)인 걸로 알고 있습니다
# def solution(prices):
#     answer = [0] * len(prices)
#
#     for idx, price in enumerate(prices):
#         for left in prices[idx+1:]:
#             answer[idx] += 1
#             if left < price:
#                 break
#
#     return answer

### 그래서 range로 다시 풀어서 성공!
def solution(prices):
    answer = [0] * len(prices)

    for idx in range(len(prices)):
        for left in range(idx+1, len(prices)):
            answer[idx] += 1
            if prices[left] < prices[idx]:
                break

    return answer

### TEST 1
prices = [1, 2, 3, 2, 3]
print(solution(prices)) # [4, 3, 1, 1, 0]