'''
백준 알고리즘
https://www.acmicpc.net/problem/1021
회전하는 큐

2021.08.10
다른 사람 풀이
deque부분을 직접 사용하지 않고 간접적으로 사용한 사례
'''

import sys

N, M = map(int, sys.stdin.readline().split())
dq = [i+1 for i in range(N)]

cnt = 0

for find in map(int, sys.stdin.readline().split()):
    idx = dq.index(find)
    cnt += min(len(dq[idx:]), len(dq[:idx]))
    dq = dq[idx + 1:] + dq[:idx] # 연산 후 결과 모습의 패턴

print(cnt)