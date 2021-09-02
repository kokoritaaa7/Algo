'''
백준 알고리즘
https://www.acmicpc.net/problem/1021
회전하는 큐

2021.08.10
'''

'''
문제 이해

3가지 연산
1. 첫 번째 원소 뽑기(popleft()) a1, a2, ... , ak => a2, ... , ak
2. 왼쪽으로 이동(rotate(-1)) a1, a2, ..., ak => a2, ..., ak, a1 
3. 오른쪽으로 이동(rotate(1)) a1, a2, ..., ak => ak, a1, a2, ..., ak-1

2,3번 연산의 최솟값 출력


[예시 1]
10 3
1 2 3

dq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
1번 연산만 3개 하면
1 2 3 순서로 도출됨 => 따라서 0

[예시 2]
10 3
2 9 5

dq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2번 연산 -> [2, 3, ..., 10, 1] cnt = 1
1번 연산 -> [3, 4, 5, ..., 10, 1] 남은 arr = 9 5
3번 연산 -> [1, 3, 4, ..., 9, 10] cnt = 2
3번 연산 -> [10, 1, 3, ..., 8, 9] cnt = 3
3번 연산 -> [9, 10, 1, 3, ..., 7, 8] cnt = 4
1번 연산 -> [10, 1, ..., 7, 8] 남은 arr = 5
5는 idx = 5에 있으므로 3번연산을 해야 최소값 갖게됨
3번 연산 -> [8, 10, 1, ..., 6, 7] cnt = 5
3번 연산 -> [7, 8, 10, 1, ..., 5, 6] cnt = 6
3번 연산 -> [6, 7, ..., 4, 5] cnt = 7
3번 연산 -> [5, 6, ..., 3, 4] cnt = 8
1번 연산 -> [6, 7, ..., 3, 4]

'''

import sys
from collections import deque

# N : 큐의 크기, M : 뽑아내려는 수의 개수)
N, M = map(int, sys.stdin.readline().split())
# arr : 뽑아내려는 데이터
arr = list(map(int, sys.stdin.readline().split()))

# 주어진 양방향 순환 큐
dq = deque(n+1 for n in range (N))

cnt = 0 # 결과값

while arr:
    # arr[0]이 있는 인덱스 찾기
    idx = dq.index(arr[0])

    if idx == 0:
        dq.popleft()
        arr.pop(0)
    elif idx < len(dq) - idx: # 2번 연산
        dq.rotate(-idx)
        cnt += idx
    else: # 3번 연산
        dq.rotate(len(dq) - idx)
        cnt += len(dq) - idx

## 얘가 좀 더 느리네? ##
# for a in arr:
#     idx = dq.index(a)
#
#     if idx == 0:
#         dq.popleft()
#     elif idx < len(dq) - idx: # 2번 연산
#         dq.rotate(-idx)
#         cnt += idx
#         dq.popleft()
#     else: # 3번 연산
#         dq.rotate(len(dq) - idx)
#         cnt += len(dq) - idx
#         dq.popleft()

print(cnt)


