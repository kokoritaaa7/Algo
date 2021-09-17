'''
프로그래머스 위클리 챌린지
https://programmers.co.kr/learn/courses/30/lessons/85002
6주차 - 복서 정렬하기

2021.09.17
'''

'''
문제 이해하기
- 주어진 조건으로 정렬하는 문제 => 유형은 정렬?

조건 #1 : 전체 승률이 높은 복서 번호가 앞으로
조건 #2 : 승률 동일한 복서들 중에 자신보다 몸무게가 무거운 복서를 이긴횟수가 많은 복서가 앞
조건 #3 : 조건2까지 만족해도 동일하다면, 자기 몸무게가 무거운 복서가 앞으로
조건 #4 : 조건4까지 동일하다면, 작은 번호가 앞쪽으로
** 다른 복서랑 아직 붙어본적이 없다? => 승률 0% 

** head2head 배열의 플래그 의미 (head2head[i][j])
   - N : 두 복서가 아직 붙어본 적 없음
   - W : i+1번 복서가 j+1번 복서를 이김
   - L : i+1번 복서가 j+1 번 복서에게 짐
head2head[i][i] => 본인이므로 기본적으로 N

접근 방법
- 한 번에 조건과 관련된 모든 값을 구한 후, 정렬하기
- reverse 조건 때문에 마지막 조건인 '작은 번호'에 대해서는 (N-본인번호)로 설정하여 같이 내림차순으로 정렬되도록 하였음

1차시도 실패 => 문제 잘못 이해 
승률 = (이긴횟수)/ (진횟수 + 이긴횟수)
'''

# weights : 복서 선수들의 몸무게
# head2head : 복서 선수들의 전적
def solution(weights, head2head):
    N = len(weights)

    # 한번에 다 구하기
    total = {}
    for i in range(N):
        wcnt, lcnt, bigger = 0, 0, 0
        for j, s in enumerate(head2head[i]):
            if s == 'W':
                wcnt += 1
                if weights[j] > weights[i]:
                    bigger += 1
            elif s == 'L':
                lcnt += 1
        winRate = wcnt/(wcnt+lcnt) if (wcnt+lcnt) != 0 else 0 # 승률 구하기
        total[i+1] = (winRate, bigger, weights[i], N-i)

    # print(total)
    # 정렬 기준 조건1 > 조건2 > 조건3 > 조건4 순으로
    # answer = sorted(total, key=lambda x:(total[x][0], total[x][1], total[x][2], total[x][3]), reverse=True)
    answer = sorted(total, key=lambda x: total[x], reverse=True)
    return answer

### 충격 사건 !!!
# 파이썬의 sort()는 동률이면 그 다음 요소를 보고 정렬을 하게 됩니다.


### TEST 1
weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))

### TEST 2
weights = [145,92,86]
head2head = ["NLW","WNL","LWN"]
print(solution(weights, head2head))

### TEST 3
weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]
print(solution(weights, head2head))

### TEST 4
weights = [10, 20, 40, 40]
head2head = ['NNNW', 'NNWN', 'NLNN', 'LNNN']
print(solution(weights, head2head))