'''
42578번 다른 풀이 참고하면서 배울 내용들
'''

## 다른 사람 풀이 ##
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 # 맨 마지막 param : reduce 함수 initalize 1로 하려고
    return answer

## Counter, reduce 모듈 공부 필요 ##

# Counter
# 등장 횟수에 따른 딕셔너리 만들어줌
# 등장 횟수가 많은 값이 앞에 오도록 정렬 해줌
from collections import Counter
a = [1, 2, 3, 4, 1, 2, 3, 1, 2, 2, 5, 4, 2, 3, 1, 6, 1, 2, 4, 2]
b = Counter(a)
print(b)
print(b.most_common())
print(b.most_common(1))

'''
결과값

Counter({2: 7, 1: 5, 3: 3, 4: 3, 5: 1, 6: 1})
[(2, 7), (1, 5), (3, 3), (4, 3), (5, 1), (6, 1)]
[(2, 7)]
'''

# Reduce
# 반복 가능한 객체(iterable obj)의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
# reduce(함수, 반복가능한객체)

from functools import reduce

def f(x, y):
    return x+y

a = [1, 2, 3, 4, 5]
print(reduce(f, a)) # 15