'''
프로그래머스 2020 KAKAO BLIND
https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
괄호 변환

2021.09.05
'''

'''
문제 이해하기
괄호 개수가 맞는 것 => 균형잡힌 괄호 문자열
균형 잡힌 괄호 문자열 & 괄호 짝이 맞는것 => 올바른 괄호 문자열

문제는 균형잡힌 괄호 문자열을 올바른 괄호 문자열로 바꾸기

접근하기
(Devide and Conquer 문제인가..!?)
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''

def solution(p):
    answer = ''

    if p == '':         # 여기가 1단계
        return ''

    # 균형잡힌 문자열로 분리하기 (2단계)
    right, left = 0, 0
    checker = True # 올바른 문자열 확인 (3단계)
    for pt in p:
        if pt == '(':
            left += 1
        elif pt == ')':
            right -= 1

        if left + right == 0:
            break
        elif left + right < 0:
            checker = False

    u = p[:2*left]
    v = p[2*left:] # 여기까지가 2단계
    # print(checker)

    if checker:     # 3단계
        answer = u + solution(v)
    else:           # 4단계
        r = {'(': ')', ')': '('}
        u = u[1:-1]
        new_result = '(' + solution(v) + ')' + ''.join([r[i] for i in u])
        return new_result

    return answer

### TEST 1
p = "(()())()"
print(solution(p)) # "(()())()"

### TEST 2
p = ")("
print(solution(p)) # "()"

### TEST 3
p = "()))((()"
print(solution(p)) # "()(())()"

### TEST 4
p = ')(())(()(())'
print(solution(p))


### 틀렸던 코드 ###
### 틀린 이유 : '뒤집는다'는 말을 리스트 역순으로 이해함
# def solution(p):
#     answer = ''
#
#     if p == '':         # 여기가 1단계
#         return ''
#
#     # 균형잡힌 문자열로 분리하기 (2단계)
#     right, left = 0, 0
#     checker = True # 올바른 문자열 확인 (3단계)
#     for pt in p:
#         if pt == '(':
#             left += 1
#         elif pt == ')':
#             right -= 1
#
#         if left + right == 0:
#             break
#         elif left + right < 0:
#             checker = False
#
#     u = p[:2*left]
#     v = p[2*left:] # 여기까지가 2단계
#
#     if checker:     # 3단계
#         answer = u + solution(v)
#     else:           # 4단계
#         u = u[1:-1]
#         new_result = '(' + solution(v) + ')' + u[::-1]
#         return new_result
#
#     return answer