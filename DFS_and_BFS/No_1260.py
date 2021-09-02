'''
백준 알고리즘
https://www.acmicpc.net/problem/1260
DFS와 BFS

2021.08.10 ~ 11

## KEY ERROR 발생 ## -> 시작 노드가 간선에 걸리지 않은 경우
## 추가해서 성공 ##
'''

import sys

N, M, V = map(int, sys.stdin.readline().split())

# 그래프 만들기
graph = {}
for _ in range(M):
    nd1, nd2 = map(int, sys.stdin.readline().split())

    if nd1 in graph:
         graph[nd1].append(nd2)
    else:
        graph[nd1] = [nd2]

    if nd2 in graph:
        graph[nd2].append(nd1)
    else:
        graph[nd2] = [nd1]

## graph 정렬 필요 ##
for i in graph:
    graph[i].sort()


### DFS는 재귀 방식으로 풀어보자 ###
# dfs 방문 노드 만들기
visited = [False] * (N+1)

def dfs(graph, v, visited):
    visited[v] = True
    result = str(v) + ' '

    # 시작노드가 간선에 걸리지 않은 경우
    if v not in graph:
        return v

    for i in graph[v]:
        if not visited[i]:
            result += dfs(graph, i, visited)

    return result.rstrip()

### BFS는 Queue 사용해서 ###
from collections import deque

def bfs(graph, v):
    visited = []
    queue = deque([v])
    # queue.append(v)

    # 시작노드가 간선에 걸리지 않은 경우
    if v not in graph:
        return v

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return ' '.join(map(str, visited))

print(dfs(graph, V, visited))
print(bfs(graph, V))