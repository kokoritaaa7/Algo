'''
백준 알고리즘
https://www.acmicpc.net/problem/18258
큐 2

2021.08.03
'''

'''
문제 이해
처음 입력받은 숫자만큼 명령어를 입력받을 수 있으며,
push는 큐에 데이터를 넣는 것, pop은 가장 앞에 있는 정수를 빼는 것
size는 큐에 있는 개수 출력, empty는 비어있으면 1 아니면 0 출력
front는 가장 앞에있는 정수 출력, back은 가장 뒤에있는 정수 출력 
'''

import sys
from collections import deque

def checkQueue(cmd):
    if 'front' in cmd:
        if len(q) == 0:
            return -1
        return q[0]
    elif 'back' in cmd:
        if len(q) == 0:
            return -1
        return q[-1]
    elif 'size' in cmd:
        return len(q)
    elif 'pop' in cmd:
        if len(q) == 0:
            return -1
        return q.popleft()
    elif 'empty' in cmd:
        if len(q) == 0:
            return 1
        return 0

cmdCnt = int(input())
q = deque()
for _ in range(cmdCnt):
    cmd = sys.stdin.readline().split()

    if len(cmd) < 2:
        print(checkQueue(cmd[0]))
    else:
        q.append(cmd[1])







