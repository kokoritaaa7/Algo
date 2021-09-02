'''
백준 알고리즘
https://www.acmicpc.net/problem/1874
스택 수열

2021.07.30
'''

## 문제 이해하기
'''
[예제 1]
8 4 3 6 8 7 5 2 1

이면 
4까지 push -> [1, 2, 3, 4] -> + + + +
4를 pop -> [1, 2, 3] -> -
3을 pop -> [1, 2] -> -
6까지 push -> [1, 2, 5, 6] -> + +
6을 pop -> [1, 2, 5] -> -
8까지 push -> [1, 2, 5, 7, 8] -> + +
8을 pop -> [1, 2, 5, 7] -> - 
7을 pop -> [1, 2, 5] -> -
5, 2, 1을 pop -> [] -> - - -

[예제 2]
5 1 2 5 3 4

이면
1까지 push -> [1] -> +
2까지 push -> [1, 2] -> +
5까지 push -> [1, 2, 3, 4, 5] -> + + +
5 pop -> [1, 2, 3, 4] -> -
3 pop -> [1, 2] -> - - 
4 pop -> NO
'''


# cmd > cnt : cmd == cnt될때까지 넣기
# cmd == cnt : pop
# cmd < cnt : pop / NO

import sys
arrLen = int(input())

def stackSeries(arrLen):
    stack = []
    result = ''
    cnt = 1

    for _ in range(arrLen):
        cmd = int(sys.stdin.readline())

        # cmd >= cnt 일 때
        while cmd >= cnt:
            stack.append(cnt)
            result += '+\n'
            cnt += 1

        # cmd < cnt 일 때

        while stack:
            if stack[-1] >= cmd:
                stack.pop()
                result += '-\n'
                break
            else:
                # 이렇게 하고 밑에서 그냥 print만 해주는게 더 효과적일듯
                return 'NO'
                # return False

    return result

result = stackSeries(arrLen)
# print(result.rstrip()) if result else print('NO')
print(result.rstrip())













## 1차시도 실패 ##
# import sys
#
# def stackSequence(arrLen):
#     stack = []
#     result = ''
#     for i in range(1, arrLen+1):
#         cmd = int(sys.stdin.readline())
#         if cmd > i:
#             stack.append(i)
#             result += '+\n'
#         elif cmd == i:
#             result += '+\n-\n'
#         else: # cmd < i
#             if stack[-1] < cmd:
#                 return False
#
#             while not stack: # stack이 empty일 때 까지
#                 if stack[-1] >= cmd:
#                     stack.pop()
#                     result = '-\n'
#     return result
#
# ## Main ##
# arrLen = int(input())
# result = stackSequence(arrLen)
# print(result) if result else print('NO')


