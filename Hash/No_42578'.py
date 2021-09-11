'''
프로그래머스 [해시]
https://programmers.co.kr/learn/courses/30/lessons/42578
위장

2021.09.11
'''

'''
문제 이해하기
- 스파이는 매일 다른 옷 조합 입어야 함
- 하루에 최소 1개의 의상은 입음

접근 방식 #1 ==> 실패
a : 3, b : 2, c : 1 (a,b,c는 종류고 그 아래가 해당 카테고리 옷 개수일때)
1. 하나씩만 입었을 때 => 3 + 2 + 1 => 6
2. 두개씩만 입었을 때 => 3*2 + 3*1 + 2*1 => 11
3. 세개씩 입었을 때 => 3 * 2 * 1 => 6

즉, 딕셔너리 구하고 계산하기

접근 방식 #2 
- 딕셔너리 구하고 계산할 때 조합 하나하나 계산하지말고!!
- (얼굴 종류 + 1) * (머리 종류 + 1) * (바지 종류 + 1) -1 
- 여기서 +1은 해당 종류의 옷을 안입는 상황의 경우의 수를 넣어줌
- 마지막의 -1은 모두 안입은 상황에 대한 경우의 수를 제외해줌
'''

def solution(clothes):
    answer = 1
    count = {}

    # 딕셔너리 만들기
    for name, category in clothes:
        count.setdefault(category, 0) # 없으면 해당 key에 대해 0으로 default 해주는 것 -> if문 대신 쓰려고
        count[category] += 1

    # 계산하기
    for i in count.values():
        answer *= (i + 1)

    return answer - 1


### 시간 초과 ###
# from itertools import combinations
#
# def multiple(tuple):
#     result = 1
#
#     for i in tuple:
#         result = result * i
#
#     return result
#
# def solution(clothes):
#     answer = 0
#     count = {}
#
#     # 딕셔너리 만들기
#     for name, category in clothes:
#         if category not in count:
#             count[category] = 1
#         else:
#             count[category] += 1
#
#         answer += 1 # 한 개씩 입을 때 계산
#
#     # 계산하기
#     idx = 1
#
#     while idx < len(count):
#         idx += 1
#         for result in combinations(count.values(), idx):
#             answer += multiple(result)
#
#     return answer


### TEST 1
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) # 5

### TEST 2
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes)) # 3