'''
백준 알고리즘
https://www.acmicpc.net/problem/1012
유기농 배추

2021.08.13 ~ 17
'''

import sys

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
farm = []

def dfs(m, n):
    if not ((-1 < m < len(farm[0])) and (-1 < n < len(farm))):
        return False

    if farm[n][m] == 1:
        farm[n][m] = 0
        for d in range(4):
            r, c = m + row[d], n + col[d]
            dfs(r, c)
        return True
    return False

for _ in range(int(sys.stdin.readline())):
    # M : 가로 길이 : row
    # N : 세로 길이 : col
    # K : 배추 위치 개수
    M, N, K = map(int, sys.stdin.readline().split())
    # M, N, K = 5, 3, 6
    farm = [[0 for _ in range(M)] for _ in range(N)]

    # 배추밭 만들기
    for _ in range(K):
      r, c = map(int, sys.stdin.readline().split())
      farm[c][r] = 1

    # dfs 검사
    cnt = 0
    for c in range(N):
        for r in range(M):
            if dfs(r, c):
                cnt += 1

    print(cnt)

