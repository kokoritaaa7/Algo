'''
프로그래머스 [완전탐색]
https://programmers.co.kr/learn/courses/30/lessons/42839
소수 찾기

2021.09.24
'''

'''
문제 이해 하기
numbers에 있는 숫자를 조합해서 소수 몇개 만들 수 있는지 출력

접근 방법 1 -> for문에서 zip(numbers, i) 이렇게 해서 소수인지 확인? => zip은 두개가 모두 iterable 이어야함 => 따라서 X
zip이 아니라 permutations 였음!!
'''


def isPrimeNum(num):
    '''소수 판별 함수'''
    import math

    if num == 1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    from itertools import permutations

    answer = set()

    for i in range(1, len(numbers)+1): # 순열 만들기 위한 for문
        visited = list(set(permutations(numbers, i))) # n개로 만들 수 있는 숫자조합 만들기
        for arr in range(len(visited)):
            num = int(''.join(visited[arr]))
            if isPrimeNum(num):
                answer.add(num)

    return len(answer)

### TEST 1
numbers = "17"
print(solution(numbers)) # 3

### TEST 2
numbers = "011"
print(solution(numbers)) # 2

