'''
이것이 코딩테스트다 with 파이썬
예제 3-2. 큰 수의 법칙

2021.10.24
'''

#### 나의 풀이법 ####
# 첫째줄에 N, M, K
# N : 배열의 크기
# M : 숫자가 더해지는 횟수
# K : 같은 인덱스 초과할 수 없는 횟수
import sys
N, M, K = map(int, sys.stdin.readline().split())

# 두번째 줄에 N
nlist = list(map(int, sys.stdin.readline().split()))
# 큰 순서대로 정렬하기
nlist.sort()

# 결과값 저장 변수
result = 0

# M번 만큼 반복
for i in range(1, M+1):

    # K를 초과니까 K+1로 설정
    if i % (K+1):
        result += nlist[-1]
    else:
        result += nlist[-2]

print(result)

#### 더 효율적으로 풀어보자 ####
'''
수학적 아이디어!
반복되는 수열에 대해서 파악하기

반복되는 수열의 길이는? K+1 
M을 K+1로 나눈 몫이 수열이 반복되는 횟수
여기에 K를 곱해주면? 가장 큰 수가 등장하는 횟수

** M이 K+1로 나누어 떨어지지 않는 경우라면?
M을 K+1로 나눈 나머지만큼 가장 큰 수가 추가됨 
'''
import sys
N, M, K = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()

# 가장 큰 수가 더해지는 횟수 계산하기
count = int(M / (K+1)) * K
count += M % (K+1)

result = count * nlist[-1] # 가장 큰 수 더하기
result += (M - count) * nlist[-2] # 두번째 큰 수 더하기

print(result)
