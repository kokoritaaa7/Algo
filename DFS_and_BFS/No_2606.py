'''
백준 알고리즘
https://www.acmicpc.net/problem/2606
바이러스

2021.08.11
'''

'''
문제 이해하기

1. 주어진 입력값으로 그래프를 만들기 (무방향 그래프)
2. 그래프를 DFS나 BFS로 접근하기 => deeue 필요
'''

from collections import deque
import sys

# 컴퓨터의 수
N = int(sys.stdin.readline())

# 그래프 만들기
# 두 개 다 해봤는데 시간은 똑같고, 아래 방법이 메모리 살짝 더 적게 먹음
graph = {i:[] for i in range(N+1)}
# graph = {}

# 연결된 쌍의 수는 바로 입력받기 -> 어짜피 인덱스 안쓰니까
for _ in range(int(sys.stdin.readline())):
    node1, node2 = map(int,sys.stdin.readline().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

    # if node1 in graph:
    #     graph[node1].append(node2)
    # else:
    #     graph[node1] = [node2]
    #
    # if node2 in graph:
    #     graph[node2].append(node1)
    # else:
    #     graph[node2] = [node1]

# print(graph)

### BFS로 접근 ###
dq = deque([1])
visited = {}
while dq:
    virus = dq.popleft()
    if virus not in visited:
        visited[virus] = 1
        dq.extend(graph[virus])

print(len(visited)-1) # 1은 제외해야 하니까

### DFS로 접근 ###
# dq = deque([1])
# visited = {}
# while dq:
#     virus = dq.pop()
#     if virus not in visited:
#         visited[virus] = 1
#         dq.extend(graph[virus])
#
# print(len(visited)-1)