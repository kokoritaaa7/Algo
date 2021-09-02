'''
백준 알고리즘
https://www.acmicpc.net/problem/1966
프린터 큐

2021.08.09
다른 사람 코드 참고
'''

import sys
testCase = int(input())

for _ in range(testCase):
    num, idx = tuple(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    max_arr = sorted(arr, reverse=True)
    j = 0
    k = 0
    while True:
        if arr[j] == max_arr[k]:
            cnt += 1
            if j == idx:
                print(cnt)
                break
            k += 1
        j = (j+1) % num