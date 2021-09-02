'''
백준 알고리즘
https://www.acmicpc.net/problem/2178
미로 탐색

2021.08.17
다른 사람 풀이 참고함
[참고] https://daimhada.tistory.com/82
'''

import sys
from collections import deque

c, r = map(int, sys.stdin.readline().split())

graph = []
for i in range(c):
    graph.append([])
    cmd = sys.stdin.readline().rstrip()
    for j in cmd:
        graph[i].append(int(j))

## (0,0)에서 (n,m)으로 가는 최단거리 구하기
## BFS ##
#
# row = [-1, 0, 1, 0]
# col = [0, -1, 0, 1]
#
# # 시작점은 들어가있음
# route = deque([(0,0)])
# result = deque()
#
# while (c-1, r-1) not in result:
#     y, x = route.popleft()
#
#     check = 0
#     for i in range(4):
#         ny, nx = y + col[i], x + row[i]
#         if (-1 < ny < c) and (-1 < nx < r) and (graph[ny][nx] == 1):
#             check += 1
#             route.appendleft((ny, nx))
#
#     if graph[y][x] == 1:
#         graph[y][x] =
#         result.append((y, x))
#
#     elif check == 0:
#         temp = result.pop()
#         route.appendleft(temp)
#
# print(len(result))
# print(result)
### 풀고보니 이거 DFS임 ###


row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]

# 시작점은 들어가있음
route = deque([(0,0)])
while route:
    y, x = route.popleft()
    # value = graph[y][x]
    for i in range(4):
        ny, nx = y + col[i], x + row[i]
        if not ((-1 < ny < c) and (-1 < nx < r)):
            continue

        #  or value + 1 < graph[ny][nx]
        if graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            route.append((ny,nx))

print(graph[c-1][r-1])
print(graph)
