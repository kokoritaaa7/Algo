'''
프로그래머스 2020 KAKAO BLIND
https://programmers.co.kr/learn/courses/30/lessons/60059
자물쇠와 열쇠

2021.09.07
'''

'''
문제 이해 하기
key는 M*M 2차원 배열
lock은 N*N 2차원 배열
(M <= N)

배열 내에서 0은 홈부분 1은 돌기부분
lock의 0 부분에 key의 1부분이 딱 맞아야 함

[접근 방식 - 실패]
1. 일단 lock의 0 부분을 찾아서 배열에 저장하고
2. key 1 부분 찾아서 배열에 저장 
3. lock 홈에 대한 거리 구하기
4. key 돌기에 대한 거리 구하기
5. lock 홈 거리 차이가 key 돌기 거리 차이 다른게 1개라도 있으면 False

[접근 방식 2 - 성공]
1. 맵을 새로 생성 (M + 2*(N -1) 의 2차원 배열로)
2. (M, M)부터 lock 채우기
3. 새로운 맵에서 lock 좌표 확인
4. key dolgi 확인하기
5. key dolgi (0,0) ~ (n-1, n-1)까지 하나씩 검사
6. key 90도 돌려서 5번을 반복
7. 5~6 과정에서 조건에 맞으면 true, 총 반복할 때까지 조건에 맞지 않으면 false

'''

def rotate(arr, M):
    ''' 90도 회전하는 함수 '''
    # (a, b) -> 90도 회전 -> (b, M-1-a)
    new_arr = []
    for a, b in arr:
        new_arr.append((b, M-1-a))
    return new_arr

def solution(key, lock):
    M, N = len(key), len(lock)

    # 새로운 맵 생성
    newMap = [[0 for i in range(M+2*(N-1))] for i in range(M+2*(N-1))]

    # lock 채우기 / lock 홈 확인하기
    lockHole = []
    for i in range(N):
        for j in range(N):
            newMap[M+i-1][M+j-1] = lock[i][j]
            if lock[i][j] == 0:
                lockHole.append((M+i-1,M+j-1))

    # key 돌기 확인하기
    keyDolgi = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                keyDolgi.append((i,j))

    def isMatch(i, j):
        cnt = 0
        for p, q in keyDolgi:
            if newMap[p+i][q+j] == 1:
                return False

            if (p + i, q + j) in lockHole:
                cnt += 1

        if cnt == len(lockHole):
            return True

        return False

    for _ in range(4):
        for i in range(N+M-1):
            for j in range(N+M-1):
                if isMatch(i,j):
                    return True

        keyDolgi = rotate(keyDolgi, M)

    return False

### 아예 잘못된 접근 ###
# def solution(key, lock):
#
#     lockHole = []
#     for i in range(len(lock)):
#         for j in range(len(lock[i])):
#             if lock[i][j] == 0:
#                 lockHole.append((i,j))
#
#     keyDolgi = []
#     for i in range(len(key)):
#         for j in range(len(key[i])):
#             if key[i][j] == 1:
#                 keyDolgi.append((i,j))
#
#     lockDist = []
#     for i in range(len(lockHole)):
#         for j in range(i+1, len(lockHole)):
#             preL, preR = lockHole[i]
#             nextL, nextR = lockHole[j]
#             lockDist.append((nextL-preL)**2 + (nextR-preR)**2)
#
#     keyDist = []
#     for i in range(len(keyDolgi)):
#         for j in range(i+1, len(keyDolgi)):
#             preL, preR = keyDolgi[i]
#             nextL, nextR = keyDolgi[j]
#             keyDist.append((nextL - preL) ** 2 + (nextR - preR) ** 2)
#
#     while lockDist:
#         if lockDist.pop(0) not in keyDist:
#             return False
#
#     return True


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock)) # True
