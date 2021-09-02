'''
백준 알고리즘
https://www.acmicpc.net/problem/1966
프린터 큐

2021.08.06 ~ 2021.08.09
'''

# import sys
# from collections import deque

testCase = int(input())

def printerqueue():
    import sys
    from collections import deque

    cnt = 0

    # num : 문서의 개수
    # idx : 현재 인덱스
    num, idx = tuple(map(int,sys.stdin.readline().split()))

    # dq : 중요도 (cmd1[0]개 만큼 입력받게 됨)
    dq = deque(map(int, sys.stdin.readline().split()))

    while dq:
        maxNum = max(dq) # O(N)
        if maxNum == dq[0]:
            cnt += 1
            dq.popleft()
            idx -= 1
        else:
            dq.rotate(-1)
            # dq.append(dq.popleft())
            if idx == 0:
                idx = len(dq) - 1
            else:
                idx -= 1

        if idx == -1:
            return cnt

    return cnt

for _ in range(testCase):
    print(printerqueue())





