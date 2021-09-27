'''
백준 알고리즘
https://www.acmicpc.net/problem/2178
미로 탐색

2021.09.24
한달도 더 지난 복습!
'''

'''
문제 이해 하기
n : row 수
m : column 수
N x M 배열에 미로가 표기되어 있음 
-> 1은 이동 가능, 0은 이동 불가능 
-> (1,1)에서 출발하여 (N,M)위치로 이동할 때 지나야하는 최소 칸 수
'''

# import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().split())
# miro = []
# for _ in range(N):
#     miro.append(list(map(int,list(sys.stdin.readline().rstrip()))))
#
# road = deque([[0, 0, 1]])
# # visited = []
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# while road:
#     r,c,cnt = road.popleft()
#
#     for i in range(4):
#         nr, nc = dr[i] + r, dc[i] + c
#
#         if nr == N-1 and nc == M-1:
#             print(cnt+1)
#             road = None
#             break
#
#         # -1 < nr < N 이면 괜찮음 + -1 < nc < M 이면 괜찮음
#         elif not (-1 < nr < N and -1 < nc < M):
#             continue
#         # elif (nr, nc) in visited: # 중복 방지! -> 탐색이 오래걸리는 거같아서
#         #     continue
#
#         # if miro[nr][nc] == 1:                 # 1인 길만 갈 수 있으니까
#         #     # visited.append((nr, nc))            # 방문지 추가해주고
#         #     road.append([nr, nc, cnt + 1])      # 새로운 길에 추가
#         if miro[nr][nc] == 1 or miro[nr][nc] > cnt+1:
#             miro[nr][nc] = cnt + 1
#             road.append([nr, nc, cnt + 1])


### NEW



import sys
from collections import deque

answer = 0
N, M = map(int, sys.stdin.readline().split())
miro = []
for _ in range(N):
    miro.append(list(map(int,list(sys.stdin.readline().rstrip()))))

road = deque([[0, 0]])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while road:
    r,c = road.popleft()

    for i in range(4):
        nr, nc = dr[i] + r, dc[i] + c

        if nr == N-1 and nc == M-1:
            answer = miro[r][c] + 1
            road = None
            break

        # -1 < nr < N 이면 괜찮음 + -1 < nc < M 이면 괜찮음
        elif not (-1 < nr < N and -1 < nc < M):
            continue

        if miro[nr][nc] == 1 or miro[nr][nc] > miro[r][c]+1:
            miro[nr][nc] = miro[r][c] + 1
            road.append([nr, nc])

print(answer)




