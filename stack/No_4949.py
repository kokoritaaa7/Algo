'''
백준 알고리즘
https://www.acmicpc.net/problem/4949
균형잡힌 세상

2021.07.29
'''

## 1번 방법 : 하나의 배열에 스택을 직접 넣어서
# from sys import stdin
# cmdStr = stdin.readline().rstrip()
#
# while cmdStr != '.':
#     stack = list()
#     for s in cmdStr:
#         if s == '(' or s == '[':
#             stack.append(s)
#         elif s == ')':
#             if len(stack) == 0:
#                 stack.append(s)
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#             else:
#                 break
#         elif s == ']':
#             if len(stack) == 0:
#                 stack.append(s)
#                 break
#             elif stack[-1] == '[':
#                 stack.pop()
#             else:
#                 break
#     if stack:
#         print('no')
#     else:
#         print('yes')
#
#     # 다음 문장 입력받기
#     cmdStr = stdin.readline().rstrip()

##  1번 방법을 좀 더 간단하게 ##
from sys import stdin

def isBalance(cmdStr):
    stack = []
    for i in cmdStr:
        if i in '([':
            stack.append(i)
        elif i ==')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

    if stack:
        return False

    return True

while True:
    cmdStr = stdin.readline().rstrip()
    if cmdStr =='.':
        break
    print('yes') if isBalance(cmdStr) else print('no')


## 2번 방법 : 두 개의 변수로 스택의 의미만 따서
### 2번 방법  -> X ([)] 를 구분할 수 없음
# from sys import stdin
#
# cmdStr = stdin.readline().rstrip()
# while cmdStr != '.':
#     stackOne = 0
#     stackTwo = 0
#     for s in cmdStr:
#         if s == '(':
#             stackOne += 1
#         elif s == ')':
#             stackOne -= 1
#             if stackOne < 0:
#                 break
#         elif s == '[':
#             stackTwo += 1
#         elif s == ']':
#             stackTwo -= 1
#             if stackTwo < 0:
#                 break
#     if stackOne == 0 and stackTwo == 0:
#         print('yes')
#     else:
#         print('no')
#     cmdStr = stdin.readline().rstrip()

