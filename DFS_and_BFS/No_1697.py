'''
백준 알고리즘
https://www.acmicpc.net/problem/1697
숨바꼭질

2021.09.01
'''

### 시간초과 해결된 방식
# import sys
# from collections import deque
#
# def BOJ_1697(n):
#     day = 0
#     result = deque([[n, day]])
#     while result:
#         now, d = result.popleft()
#         if not visited[now]:
#             visited[now] = True
#             if now == k:
#                 return d
#             d += 1
#             if (now * 2) < 100001:
#                 result.append([now * 2, d])
#             if (now + 1) < 100001:
#                 result.append([now + 1, d])
#             if (now - 1) >= 0:
#                 result.append([now - 1, d])
#     return d
#
#
# n, k = map(int, sys.stdin.readline().split())
# visited = [False] * 100001
# print(BOJ_1697(n))


### 런타임에러 / 틀렸습니다 (11%)
### 해결 : 100001로 넉넉하게 줘서..
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

def BFS(N, K):
    if N == K:
        return 0

    bfs_checker = deque([N])
    arr = [0] * 100001
    arr[N] = 1

    while bfs_checker:
        n = bfs_checker.popleft()

        check = [n-1, n+1, 2*n]
        for i in range(3):
            if check[i] == K:
                arr[check[i]] = arr[n]+1
                return arr[n]
            elif check[i] > 0 and check[i] < 100001 and arr[check[i]] == 0:
                arr[check[i]] = arr[n] + 1
                bfs_checker.append(check[i])

    return arr[K] - 1

print(BFS(N, K))



## 시간 초과 (8%)
# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
# cnt = 0
# arr = [False] * 100001
# bfs_checker = deque([N])
#
# while arr[K] is False:
#     temp = set()
#     while bfs_checker:
#         n = bfs_checker.popleft()
#
#         if arr[n]: # 이미 간 곳은 못가도록
#             continue
#         else:
#             arr[n] = True
#
#         if n == K:
#             break
#
#         if 0 < n+1 <= K:
#             temp.add(n+1)
#         if 0 < n-1 <= K:
#             temp.add(n-1)
#         if 0 < 2*n <= K:
#             temp.add(2*n)
#
#     cnt += 1
#     bfs_checker = deque(temp)
#
# print(cnt-1 if cnt != 0 else cnt)


### 시간 초과 코드 (2%)
# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
# cnt = 0
# bfs_checker = deque([N])
# while K not in bfs_checker: # bfs_checker에 동생 좌표 있으면 멈춤
#     temp = set() # 같은 수 연산 횟수 줄여주려고
#     while bfs_checker:
#         n = bfs_checker.popleft()
#
#         if (n == K) or (n < 0) or (n > K):
#             break
#
#         temp.add(n+1)
#         temp.add(n-1)
#         temp.add(2*n)
#
#     cnt += 1
#     bfs_checker = deque(temp)
#
# print(cnt)