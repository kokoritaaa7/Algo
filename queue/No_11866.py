'''
백준 알고리즘
https://www.acmicpc.net/problem/11866
요세푸스 문제 0

2021.08.05
'''

'''
문제 이해
N = 7, K = 3
<1, 2, 3, 4, 5, 6, 7>
1번째로 3 삭제 <1, 2, 4, 5, 6, 7>
2번째로 6 삭제 <1, 2, 4, 5, 7>
3번째로 2 삭제 <1, 4, 5, 7>
4번째로 7 삭제 <1, 4, 5>
5번째로 5 삭제 <1, 4>
6번째로 1 삭제 <4>
7번째로 4 삭제 <1>
=> [3, 6, 2, 7, 5, 1, 4]

접근 방법 # 1 : 원형 큐
접근 방법 # 2 : idx로 계산
'''

# 리스트로 원형 큐 처럼 만들기 (시간초과 예상됨..)

# result = []
# N, K = tuple(map(int, input().split()))
#
# arr = [n+1 for n in range(N)]
#
# while arr:
#     idx = 0
#     while idx != (K-1):
#         arr.append(arr.pop(0))
#         idx += 1
#
#     result.append(arr.pop(0))
#
# print(result)

# deque로도 가능
# from collections import deque
#
# # result = []
# result = '<'
# N, K = tuple(map(int, input().split()))
#
# arr = deque(n+1 for n in range(N))
#
# while arr:
#     idx = 0
#     while idx != (K-1):
#         arr.append(arr.popleft())
#         idx += 1
#
#     # result.append(str(arr.popleft()))
#     result += str(arr.popleft()) + ', '
#
# print(result[:-2]+'>')
# # print('<', ', '.join(result), '>', sep='') # 얘가 시간 더 오래걸림


# 원형큐 사용하기 - rotate()
from collections import deque

N, K = tuple(map(int, input().split()))
dq = deque(n+1 for n in range(N))
result = []

while dq:
    dq.rotate(-K + 1)
    result.append(str(dq.popleft()))

print('<', ', '.join(result), '>', sep='')

