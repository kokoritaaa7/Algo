'''
백준 알고리즘
https://www.acmicpc.net/problem/7576
토마토

2021.08.19
원래 2021.08.18에 풀었어야 함 ㅎㅎ
'''

'''
문제 이해하기
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
이전 '미로 찾기'와 비슷하게 진행하면 되지 않을까? 

반례 존재하는 듯 ㅠ_ㅠ
반례 해결하였으나 시간 초과 > 해결
(반례)
3 3
1 1 -1
-1 0 0
0 0 0

답 : 3
'''

import sys
from collections import deque

x,y = map(int, sys.stdin.readline().split())

tomatoBox = []
tomato = deque()
zero_count = 0
for idx in range(y):
    cmd = list(map(int, sys.stdin.readline().split()))
    tomatoBox.append(cmd)
    for j in range(len(cmd)):
        if cmd[j] == 1:
            tomato.append((idx, j)) # y, x로 저장
        elif cmd[j] == 0:
            zero_count += 1

# print(tomatoBox)
# print(tomato)
### 여기까지 박스 완성 - 테스트도 완료 ###

def BeakJoon7576(zero_count):
    col = [0, 1, 0, -1]
    row = [1, 0, -1, 0]
    count = set()

    while tomato:
        c, r = tomato.popleft()

        for i in range(4):
            nc, nr = col[i] + c, row[i] + r
            if not ((-1 < nc < y) and (-1 < nr < x)):
                continue

            if tomatoBox[nc][nr] == 0:
                zero_count -= 1
                tomatoBox[nc][nr] = tomatoBox[c][r] + 1
                tomato.append((nc, nr))
                count.add(tomatoBox[nc][nr])

                # if tomatoBox[c][r] not in count:
                #     count.append(tomatoBox[c][r])

    print(len(count) if zero_count == 0 else -1)

if zero_count == 0:
    print(0) # 그 뒤에 동작은 안해도 됨
else:
    BeakJoon7576(zero_count)




### 문제 발생 ###
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
# 0 출력 방법 -> input 때 zero count 확인해서 0없으면 시작도 안하는 방법
### 해결 -> zero_count 변수 추가해서 애초에 0이면 시작안하고, 처리 후, 0보다 크면 -1 출력

### 문제 발생 2 ###
# deque에 1 인덱스 넣을 때 제일 앞에있는 것만 넣어서 해당 배열에 여러개 있어도 하나만 추가됨
# 대안1 - elif tomatoBox[nc][nr] == 1하면 무한루프 됨 ==> 실패
# 대안2 - visited 배열 넣어서 거기에 있으면 skip? ==> 성공헸으나 시간초과 (2%에서)
# 대안3 - 애초에 박스 만들 때 for문 돌려서 넣어주기 ==> 얘도 시간초과 (40%정도에서)

### 문제 발생 3 ###
# 시간 초과 문제 발생
### 해결 -> count를 배열이 아닌 set 집합으로 바꿔줌