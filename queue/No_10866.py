'''
백준 알고리즘
https://www.acmicpc.net/problem/10866
덱

2021.08.09
'''

import sys
from collections import deque

N = int(input())
dq = deque()
for _ in range(N):
    cmd = sys.stdin.readline()

    if cmd[0] == 's':
        print(len(dq))
    elif cmd[0] == 'e':
        print(0 if dq else 1)
    elif cmd[0] == 'f':
        print(dq[0] if dq else -1)
    elif cmd[0] == 'b':
        print(dq[-1] if dq else -1)
    else:
        cmd1 = cmd.split()
        if cmd1[0] == 'push_front':
            dq.appendleft(int(cmd1[1]))
        elif cmd1[0] == 'push_back':
            dq.append(int(cmd1[1]))
        elif cmd1[0] == 'pop_front':
            print(dq.popleft() if dq else -1)
        else:
            print(dq.pop() if dq else -1)

