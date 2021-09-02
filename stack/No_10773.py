'''
백준 알고리즘
https://www.acmicpc.net/problem/10773
제로

2021.07.27
'''

import sys

# def stackZero(cmdCnt):
#     arr = list()
#     for _ in range(cmdCnt):
#         num = int(sys.stdin.readline())
#         if num == 0:
#             arr.pop()
#         else:
#             arr.append(num)
#     return sum(arr)
#
# cmdCnt = int(sys.stdin.readline())
# print(stackZero(cmdCnt))

## 다른 사람 방법 : 거의 비슷함 ##
cnt = int(sys.stdin.readline())
l=[]

# 입력받으면서 바로 int로 변환
for _ in range(cnt):
    i = int(sys.stdin.readline())
    # 0인 경우 else로 가서 pop을 바로 진행
    l.append(i) if i else l.pop()
print(sum(l))