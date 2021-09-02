'''
백준 알고리즘
https://www.acmicpc.net/problem/2164
카드 2

2021.08.04
'''

'''
문제 이해
N개의 정수가 있을 때
맨 앞의 숫자는 버리고, 그 다음 맨 앞이 된 숫자는 맨 뒤로 보내기

# 방법 1 : deque
N = 4일 때
deque = [1, 2, 3, 4]
deque.popleft() [2, 3, 4]
deque.append(deque.popleft()) [3, 4, 2]
---> 반복 
[4, 2]
[2, 4]
[4] 1개 남으면 끝

# 방법 2 : front, rear + 그냥 list
N = 4일 때 
list = [1, 2, 3, 4] 
front = 1, rear = 4

rear = front + 1 (rear = 2)
front += 2 (front = 3)
--> 반복

rear = front + 1 (rear = 4)
front += 2 (front = 5) 흠.. 
'''

# 일단 방법 1로
# from collections import deque
#
# N = int(input())
# dq = deque(n for n in range(1, N+1))
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
#
# print(dq[0])

# 방법 2 : 규칙
N = int(input())
d = 1

while N > d:
    d *= 2
    
print(N if N==d else 2 * N - d)
