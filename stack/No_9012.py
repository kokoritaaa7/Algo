'''
백준 알고리즘
https://www.acmicpc.net/problem/9012
괄호

2021.07.28
'''

# 시간복잡도 : O(N^2)
### 나의 방법 ###
# import sys
#
# num = int(sys.stdin.readline())
# for _ in range(num):
#     checker = list()
#     ps = sys.stdin.readline()
#     for p in ps:
#         if p == '(':
#             checker.append(p)
#         elif p == ')':
#             if checker:
#                 checker.pop()
#             else:
#                 checker.append(p)
#                 break;
#     if checker:
#         print('NO')
#     else:
#         print('YES')


### 다른 사람 참고 방법 ###
import sys
num = int(input())

for _ in range(num):
    ps = sys.stdin.readline().strip()
    stack = 0
    for p in ps:
        if p == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break

    print('NO') if stack else print('YES')
