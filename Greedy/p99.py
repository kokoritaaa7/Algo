'''
이것이 코딩테스트다 with 파이썬
예제 3-4. 1이 될 때까지
난이도 ●○○

2021.10.25
'''

### 나의 방법 ###
# 접근 방법: 문제 그대로 k로 나누어 떨어지면 나누고, 그렇지 않으면 -1하면서 풀이
import sys
n, k = map(int, sys.stdin.readline().split())
cnt = 0

while n != 1:
    cnt += 1
    if n % k != 0:
        n -= 1
    else:
        n = n // k

print(cnt)


### 더 효율적인 방법 ###
# 접근 방법: n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드 작성
import sys
n, k = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    # n == k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    cnt += (n - target)
    n = target

    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    cnt += 1
    n = n // k

# 마지막으로 남은 수에 대하여 1씩 빼기
cnt += (n-1)
print(cnt)