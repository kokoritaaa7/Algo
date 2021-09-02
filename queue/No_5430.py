'''
백준 알고리즘
https://www.acmicpc.net/problem/5430
AC

2021.08.10
'''

### 런타임 에러 발생 ### >> 수정 완료
### 시간 초과 ###
from collections import deque
import sys

testCase = int(input())

def AC(cmd, arr):

    # 'error'부터 잡기
    dCnt = cmd.count('D')
    if dCnt > len(arr):
        return 'error'

    isRev = 1 # 안뒤집힌 상태 (뒤집힌 상태면 -1)

    for s in cmd:
        if s == 'R':
            isRev *= -1
        elif s == 'D':
            if isRev == 1:
                arr.popleft()
            else:
                arr.pop()

    if isRev == -1:
        arr = list(arr)[::-1]

    result = '['
    for i in arr:
        result += str(i) + ','

    result = result[:-1] + ']' if len(result) != 1 else '[]'

    return result


# def AC(cmd, arr):

    ## 시간 복잡도가 어마어마 함 ##
    # for c in cmd:
    #     if c == 'R':
    #         arr.reverse()
    #     elif len(arr) == 0:
    #         return 'error'
    #     else:
    #         arr.pop(0)

    ## 방법 고안함 - 안되는 듯##
    # 1. error 유무부터 파악
    # 2. cmdarr = cmd.split('R') 해서 cmdarr내부의 D만큼 연산 하고 cmdarr len에 따라 마지막에 reverse 하는지

    # dCnt = cmd.count('D')
    # if dCnt > len(arr):
    #     return 'error'
    # rArr = cmd.split('R')
    # # 0번째 : even, 1번째 : odd , ...
    # odd = 0 # 홀수번째는 pop()
    # even = 0 # 짝수번째는 popleft()
    # # 일단 odd, event count 내서 string 인덱스로 자르기 arr[even:-(odd+1)] (-1은 끝까지니까)
    # # print(rArr)
    #
    # for i in range(len(rArr)):
    #     if i % 2 == 0:
    #         even += len(rArr[i])
    #     else:
    #         odd += len(rArr[i])
    #
    # for _ in range(even):
    #     arr.popleft()
    #
    # for _ in range(odd):
    #     arr.pop()
    #
    # # print(odd, even)
    # if len(rArr) % 2 == 0:
    #     arr.reverse()
    #
    # return list(arr)

for _ in range(testCase):
    cmd = sys.stdin.readline().rstrip().replace('RR', '') # 'RR'은 두번 뒤집는 거니까 ''로 대체하기
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(',')
    arr = [] if arr[0] == '' else deque(map(int, arr))

    print(AC(cmd, arr))


'''
NEW 방법
R 개수, D 개수 확인 
R 개수 짝수면 그대로, 홀수면 reverse
D 개수 확인해서 arr[d:]

NO 틀렸음 -> RDDRD 이런경우는 reverse 한 상태에서 D 연산 2번 하고 다시 Reverse 해야되는데 지금 알고리즘에서는 그냥 4번 D 연산을 진행함
'''
# import sys
# testCase = int(input())
# for _ in range(testCase):
#     cmd = sys.stdin.readline()
#     n = int(sys.stdin.readline())
#     arr = sys.stdin.readline()[1:-2].split(',')
#     arr = [] if arr[0] == '' else list(map(int, arr))
#
#     isReverse = False if cmd.count('R') % 2 == 0 else True
#     dCnt = cmd.count('D')
#     if isReverse:
#         arr.reverse()
#     if dCnt > len(arr):
#         print('error')
#     else:
#         print(arr[dCnt:])

