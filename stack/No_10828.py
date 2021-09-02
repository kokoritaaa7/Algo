'''
백준 알고리즘
https://www.acmicpc.net/problem/10828
스택

2021.07.26
시간초과로 인한 실패
이후 다시 성공!
'''

### 시간 초과 ###
### sys.stdin.readline 추가로 해결 ###

from collections import deque
import sys
input = sys.stdin.readline

cmdCnt = int(input())
stack = deque()
for _ in range(cmdCnt):
    cmd = input().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            max_idx = len(stack)-1
            print(stack[max_idx])


