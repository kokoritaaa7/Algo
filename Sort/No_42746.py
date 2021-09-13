'''
프로그래머스 [정렬]
https://programmers.co.kr/learn/courses/30/lessons/42746
가장 큰 수

2021.09.13
'''

## 다른 사람 풀이 참고.. ##
# [참고] https://hocheon.tistory.com/48
def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse=True)
    # x*3 해주는 이유 => 원소가 1000 이하니까 1의 자리 숫자의 경우 111 ~ 999 까지 되니까
    # TC 2의 경우 3, 30, 34 인데 그냥 정렬하면 34, 30, 3 순서대로 정렬됨
    # x * 3을 해주면 같은 문자열 3번 반복이기 때문에 => 333, 303030, 343434 => 정렬하면 34, 3, 30 순서로 정렬됨 (원하는 대로 정렬되는 것!!)

    answer = ''.join(numbers)

    return str(int(answer))

### 프로그래머스 다른 풀이 ###
### functools.cmp_to_key() 부분 설명 아래 참고
# https://frhyme.github.io/python-lib/python_lib_functools_cmp_to_keys/

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution2(numbers):
    n = map(str, numbers)
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


### 아무리 생각해도 모르겠음 ###
# def solution(numbers):
#     answer = ''
#     numbers = sorted(list(map(str, numbers)), reverse=True)
#     # answer = ''.join(numbers)
#
#     return answer


### TEST 1
numbers = [6, 10, 2]
print(solution(numbers)) # "6210"

### TEST 2
numbers = [3, 30, 34, 5, 9]
print(solution(numbers)) #"9534330"

### TEST 3
numbers = [0, 0, 0, 0]
print(solution(numbers)) # 0 (0000 나오길래 str(int(answer)) 로 해결)
