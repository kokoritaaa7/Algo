'''
백준 알고리즘
https://www.acmicpc.net/problem/7569
토마토

2021.08.21, 24
'''

import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
tomatoBox = [[] for _ in range(K)]
zero_count = 0
check = deque()

for k in range(K):
    for c in range(N):
        cmd = list(map(int, sys.stdin.readline().split()))
        tomatoBox[k].append(cmd)
        for i in range(M):
            if cmd[i] == 0:
                zero_count += 1
            elif cmd[i] == 1:
                check.append((k, c, i)) # z, y, x 순서

# print(tomatoBox)
# print(tomatoBox[0][1][2])
### 토마토 박스 완성 ###
def BeakJoon7569(zero_count):

    row = [1, 0, -1, 0, 0, 0]
    col = [0, 1, 0, -1, 0, 0]
    dim = [0, 0, 0, 0, -1, 1] # 높이
    count = set()

    while check:
        z, y, x = check.popleft()

        for i in range(6):
            r, c, k = row[i] + x, col[i] + y, dim[i] + z

            if not ((-1 < r < M) and (-1 < c < N) and (-1 < k < K)):
                continue

            if tomatoBox[k][c][r] == 0:
                zero_count -= 1
                tomatoBox[k][c][r] = tomatoBox[z][y][x] + 1
                check.append((k, c, r))
                count.add(tomatoBox[k][c][r])

    return -1 if zero_count > 0 else len(count)

if zero_count == 0:
    print(0)
else:
    print(BeakJoon7569(zero_count))
    # count, zero_count = BeakJoon7569(zero_count)
    # print(len(count) if zero_count == 0 else -1)




