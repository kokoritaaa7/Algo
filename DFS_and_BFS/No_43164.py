'''
프로그래머스 - 깊이/너비 우선 탐색(DFS/BFS)
https://programmers.co.kr/learn/courses/30/lessons/43164
여행경로

2021.10.15
'''

'''
문제 이해 하기
1. tickets을 모두 사용하고 ICN에서 출발함
2. 가능한 경로가 2개라면? 알파벳 순서로 출력

=> 일단 정렬로 알파벳 순서로 접근할 수 있도록 하고
=> DFS 적용하기 
=> 같은 이름일 때 고려를 못 함...
'''
#
# def ticketSort(tickets):
#     temp = []
#     rest = []
#     for i in range(len(tickets)):
#         if tickets[i][0] == "ICN":
#             temp.append(tickets[i])
#         else:
#             rest.append(tickets[i])
#
#     temp.sort()
#     rest.sort(reverse=True)
#
#     return temp + rest
#
# def solution(tickets):
#     answer = []
#     tickets = ticketSort(tickets)
#     fordel = tickets
#     stack = []
#
#     # ICN으로 시작하는 것들 Stack에 넣어주기
#     for ticket in tickets:
#         if ticket[0] == 'ICN':
#             stack.append(ticket)
#         else:
#             break
#
#     while True:
#         now = stack.pop(0)
#         answer.append(now)
#         fordel.remove(now)
#
#         if len(fordel) == 0:
#             return ['ICN'] + [trip[1] for trip in answer]
#
#         cnt = 0
#         for ticket in fordel:
#             if ticket[0] == now[1]:
#                 stack.insert(0, ticket)
#                 cnt += 1
#
#         if cnt == 0:
#             while True:
#                 restore = answer.pop(-1)
#                 fordel.append(restore)
#                 if restore[0] == stack[0][0]:
#                     break

from collections import defaultdict

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)
        tmp = footprint + [country]
        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

### TEST 1
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # ["ICN", "JFK", "HND", "IAD"]

### TEST 2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets)) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

### TEST 3
tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
print(solution(tickets)) # ["ICN", "B", "ICN", "A", "D", "A"]

### TEST 4
tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
print(solution(tickets)) # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

### TEST 5
tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print(solution(tickets)) # ["ICN", "COO", "ICN", "BOO", "DOO"]

### TEST 6
tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
print(solution(tickets)) # ["ICN", "SFO", "ICN", "SFO", "QRE"]

### TEST 7
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
print(solution(tickets)) # ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]