'''
백준 알고리즘
https://www.acmicpc.net/problem/2667
단지번호붙이기

2021.08.12
'''

'''
문제 이해하기

지도에서 좌우 또는 아래위로 연결된 경우 => 하나의 단지 (대각선은 X)
단지의 수를 제일 위에 출력하고, 단지에 속하는 집의 수를 오름차순으로 정렬 => result[0] + sorted(result[1:]) 
'''

# import sys
#
# N = int(sys.stdin.readline())
# # 지도 만들기
# city_map = []
#
# # for _ in range(N):
# #     city_map.append(list(map(int,list(sys.stdin.readline().rstrip()))))
#
# '''
# 방법 1
# while로 1의 인덱스를 찾아서 그 주변 확인하고, 1인 값 발견하면 0으로 바꾸기? 혹은 visited에 넣고 x,y좌표 뺀 값을 더해서 1이면 이웃
# '''
#
# '''
# while로 돌면서 1인 인덱스 찾고 -> 거리값이 1인 애들을 queue에 넣고 -> 1인지 0인지 확인 -> 1이면 queue에 넣고 0이면 queue에 안넣음?
# '''
# from collections import deque
# result = [0]
#
# dq = deque()
# for i in range(N):
#     while 1 in city_map[i]:
#         j = city_map[i].index(1)
#         dq.append((i,j))
#         result[0] += 1
#         cnt = 0
#
#         while dq:
#             y, x = dq.popleft()
#             if city_map[y][x] == 1:
#                 cnt += 1
#                 city_map[y][x] = 0
#                 if y < N - 1 and city_map[y+1][x]:
#                     dq.append((y+1, x))
#                 if y != 0 and city_map[y-1][x]:
#                     dq.append((y-1, x))
#                 if x != 0 and city_map[y][x-1]:
#                     dq.append((y, x-1))
#                 if x < N - 1 and city_map[y][x+1]:
#                     dq.append((y, x+1))
#
#             dq = deque(set(dq))
#
#         result.append(cnt)
#
# # dq = deque(city_map.index(1))
# # while True:
#
# result = [result[0]] + sorted(result[1:])
# print('\n'.join(map(str, result)))

# import sys
# N = int(sys.stdin.readline())
# # 지도 만들기
# city_map = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
#
# from collections import deque
# total_cnt = 0
# result = []
# dq = deque()
# for i in range(N):
#     while 1 in city_map[i]:
#         j = city_map[i].index(1)
#         dq.append((i,j))
#         total_cnt += 1
#         cnt = 0
#
#         while dq:
#             y, x = dq.popleft()
#             if city_map[y][x] == 1:
#                 cnt += 1
#                 city_map[y][x] = 0
#                 if y < N - 1 and city_map[y+1][x]:
#                     dq.append((y+1, x))
#                 if y != 0 and city_map[y-1][x]:
#                     dq.append((y-1, x))
#                 if x != 0 and city_map[y][x-1]:
#                     dq.append((y, x-1))
#                 if x < N - 1 and city_map[y][x+1]:
#                     dq.append((y, x+1))
#
#             dq = deque(set(dq))
#
#         result.append(cnt)
#
# print(total_cnt)
# print('\n'.join(map(str, sorted(result))))

## 1을 비교할 필요있으려나 -> 없애보기
import sys
N = int(sys.stdin.readline())
# 지도 만들기
city_map = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]

from collections import deque
total_cnt = 0
result = []
dq = deque()
for i in range(N):
    while 1 in city_map[i]:
        j = city_map[i].index(1)
        dq.append((i,j))
        total_cnt += 1
        cnt = 0

        while dq:
            y, x = dq.popleft()

            if city_map[y][x] == 0:
                continue

            cnt += 1
            city_map[y][x] = 0
            if y < N - 1 and city_map[y+1][x]:
                dq.append((y+1, x))
            if y != 0 and city_map[y-1][x]:
                dq.append((y-1, x))
            if x != 0 and city_map[y][x-1]:
                dq.append((y, x-1))
            if x < N - 1 and city_map[y][x+1]:
                dq.append((y, x+1))

            dq = deque(set(dq))

        result.append(cnt)

print(total_cnt)
print('\n'.join(map(str, sorted(result))))