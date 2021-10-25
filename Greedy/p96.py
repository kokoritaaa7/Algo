'''
이것이 코딩테스트다 with 파이썬
예제 3-3. 숫자 카드 게임
난이도 ●○○

2021.10.25
'''

# 접근방법: 행에서 가장 작은 수 뽑고 이전 행에서 뽑은 수와 비교해서 큰 숫자를 남기게 하기
import sys

r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, sys.stdin.readline().split())))

prev = 0
for num in arr:
    prev = max(min(num), prev)

print(prev)
