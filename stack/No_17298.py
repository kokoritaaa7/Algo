'''
백준 알고리즘
https://www.acmicpc.net/problem/17298
오큰수

2021.08.01
'''

'''
문제 이해하기
오큰수(NGE) : 본인보다 큰 수 중에 가장 왼쪽에 있는 수
오큰수 없으면 -1

[예시1]
A = [3, 5, 2, 7]
NGE(1) = 5 : 3의 오른쪽에 있는 수 중에 3보다 큰 수 -> 5와 7 그 중에 가장 왼쪽에 있는 수 -> 5
NGE(2) = 7 : 5의 오른쪽에 있는 수 중에 5보다 큰 수 -> 7
NGE(3) = 7 : 2의 오른쪽에 있는 수 중에 2보다 큰 수 -> 2
NGE(4) = -1 : 7의 오른쪽에 있는 수가 없으니까
'''

# ## 시간초과 ##
# import sys
# num = int(input())
# stack3 = list(map(int, sys.stdin.readline().split()))
# result = []
#
# for i in range(num):
#     j = i+1
#     fin = -1
#     while j < num:
#         if stack3[i] < stack3[j]:
#             fin = stack3[j]
#             break
#         j += 1
#
#     result.append(fin)
#
# print(*result)

import sys
num = int(input())

arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * num

for i in range(num):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]

    stack.append(i)

print(*result)