'''
프로그래머스 2020 KAKAO BLIND
https://programmers.co.kr/learn/courses/30/lessons/60061
기둥과 보 설치

2021.09.10
'''

'''
문제 이해하기
- n : 2차원 배열 n x n 에서 그림이 그려짐
- build_frame에서 순서대로 일이 진행됨
- x, y, a, b 로 들어있는데 
  x, y는 설치 좌표
  a=0이면 기등 a=1이면 보
  b=0이면 삭제 b=1이면 설치
- 기둥은 바닥 위에 있거나 보 한쪽 위에 있거나 다른 기둥위에 있어야 함
- 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어야함
- 바닥에 보 X, 벽면 벗어나게 설치 X
- 보: 오른쪽 방향으로 설치되고, 기둥 : 위쪽으로 설치되고 (해당 좌표에서 +1)
- 구조물 겹치기 X, 없는 구조물 삭제 불가
* return (output) 규칙
  - [x,y,a] => x,y는 좌표 a는 구조물 종류(0이면 기둥, 1이면 보)
  - x 좌표 기준 오름차순 정렬 > y 좌표 기준 오름차순 정렬 > a=0  

* 접근 방식 -> 실패
1. n x n 지도? 만들고
2. build_frame에서 하나씩 꺼내서 기둥과 보 설치 -> 조건에 안맞으면 버리고 
3. output 조건에 맞게 정렬

* NEW 접근 방식 (참고함)
1. 보와 기둥 배열을 각각 만들기
2. 모듈화!! 
   - 보 만들어도 되는지 확인하는 함수
   - 기둥 만들어도 되는지 확인하는 함수
   - 삭제해도 되는지 확인하는 함수
3. output 정렬 
'''

### 참고해서 풀기 ###
### 이분의 접근 방식 -> 기둥과 보를 아예 다른 배열로 봄

def check_bo(make_gd, make_bo, x, y):
    if make_gd[x][y-1] or make_gd[x+1][y-1]:
        return True
    if make_bo[x+1][y] and make_bo[x-1][y]:
        return True

    return False

def check_gd(make_gd, make_bo, x, y):
    if y == 0 or make_gd[x][y-1]: # 바닥에 붙어있거나 아래에 기둥이 있을 때
        return True

    if make_bo[x][y] or make_bo[x-1][y]: # 아래에 보가 있을 때 (보가 왼쪽/오른쪽 있을 때)
        return True

    return False

def check_delete(a, make_gd, make_bo, x, y, n):
    for i in range(n+1):
        for j in range(n+1):
            if make_bo[i][j] == 1:
                if not check_bo(make_gd, make_bo, i, j):
                    return False
            if make_gd[i][j] == 1:
                if not check_gd(make_gd, make_bo, i, j):
                    return False

    return True

def solution(n, build_frame):
    make_gd = [[0] * (n+1) for i in range(n+1)]
    make_bo = [[0] * (n+1) for i in range(n+1)]
    answer = []

    for x, y, a, b in build_frame:
        if b: # 설치일 때
            if a: # 보 설치일 때
                if check_bo(make_gd, make_bo, x, y):
                    make_bo[x][y] = 1
            else: # 기둥 설치일 때
                if check_gd(make_gd, make_bo, x, y):
                    make_gd[x][y] = 1

        else: # 삭제일 때
            if a == 0: # 기둥 삭제일 때
                make_gd[x][y] = 0
            else: # 보 삭제일 때
                make_bo[x][y] = 0

            if not check_delete(a, make_gd, make_bo, x, y, n):
                if a == 0:
                    make_gd[x][y] = 1
                else:
                    make_bo[x][y] = 1

    ## 정렬
    ## 요구사항 : x > y > 기둥 > 보
    for i in range(len(make_gd[0])):
        for j in range(len(make_gd)):
            if make_gd[i][j] == 1:
                answer.append([i, j, 0])
            if make_bo[i][j] == 1:
                answer.append([i, j, 1])

    return answer





### 테스트케이스만 맞음 ###
### 완전 틀렸음 ###
# def solution(n, build_frame):
#     answer = []
#
#     # 기둥은 0, 보는 1이니까 아무것도 없을때는 -1로 지정하기
#     wall = [[-1 for _ in range(n+1)] for _ in range(n+1)]
#
#     # x, y : 좌표
#     # a : 구조물 (0:기둥/1:보)
#     # b : 작업 (0:삭제/1:설치)
#     for x, y, a, b in build_frame:
#         # x, y 좌표 벗어나는지 부터
#         if x > n or y > n or x < 0 or y < 0:
#             continue
#         # 작업부터
#         if b: # 설치일 때
#             # 보일 때 x 좌표가 n보다 작아야함
#             if a:   # 보일 때 -> (x, y-1)에 기둥 있거나 (x-1,y)에 보가 있거나
#                 if wall[x][y-1] == 0 or wall[x+1][y-1] == 0 or wall[x][y+1] == 0:
#                     wall[x][y] = a
#                 elif wall[x-1][y] == 1 and wall[x+1][y] == 1:
#                     wall[x][y] = a
#             else: # 기둥일 때 -> 바닥이거나, 아래(x, y-1)에 기둥이나 보가 있거나
#                 if y == 0 or wall[x][y-1] == 0 or wall[x-1][y] == 1:
#                     wall[x][y] = a
#         else: # 삭제일 때
#             if wall[x][y] == -1:
#                 continue
#
#             if a == 0: # 기둥일 때 -> 위에 아무것도 없으면 삭제 가능
#                 if wall[x-1][y+1] == -1: # 아무것도 없을 때 삭제 가능
#                     wall[x][y] = -1
#                 elif wall[x-1][y+1] == 1 and wall[x+1][y+1] == 1: # 보가 양 옆으로 연결되어 있을 때
#                     wall[x][y] = -1
#
#
#     for x in range(n+1):
#         for y in range(n+1):
#             if wall[x][y] != -1:
#                 answer.append([x, y, wall[x][y]])
#
#
#     return answer


### TEST 1
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame)) # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

### TEST 2
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame)) # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]


# test = [[n+i for n in range(5)] for i in range(5)]
# print(test)
# print(test[1][2])