'''
프로그래머스 위클리 챌린지
https://programmers.co.kr/learn/courses/30/lessons/83201
2주차

2021.08.25
'''

'''
문제 이해하기
2차원 배열 -> 평가점수
i행 j열 -> i번 학생이 j번 학생 과제를 평가
학생 본인을 평가한 점수가 "유일한" 최고점 또는 최저점인 경우 -> 제외
j열 대로 평균을 매김

평균 점수가 90점 이상이면 A
80 ~ 90 이면 B
70 ~ 80 이면 C
50 ~ 70 이면 D
50 미만이면 F
'''

## 접근 1 : min, max 구해서 count가 해당 값이 1개 이상이고 i==j일 때는 빼야되나

def solution(scores):
    answer = ''

    scores_arrange = list(map(list, zip(*scores)))
    for i in range(len(scores_arrange)):
        min_score = min(scores_arrange[i])
        max_score = max(scores_arrange[i])

        cnt = 0
        if min_score == scores_arrange[i][i]:
            cnt = scores_arrange[i].count(min_score)
        elif max_score == scores_arrange[i][i]:
            cnt = scores_arrange[i].count(max_score)

        if cnt == 1:
            scores_arrange[i].pop(i)
            print(str(i) + '번째에서 삭제')

    # print(scores_arrange)
    
    # grade 매기기
    # grade = []
    # for i in range(len(scores_arrange)):
    #     avg_score = sum(scores_arrange[i]) / len(scores_arrange[i]) # 평균 점수 구하기
    #
    #     if avg_score >= 90:
    #         grade.append('A')
    #     elif avg_score >= 80:
    #         grade.append('B')
    #     elif avg_score >= 70:
    #         grade.append('C')
    #     elif avg_score >= 50:
    #         grade.append('D')
    #     else:
    #         grade.append('F')
    #
    # answer = ''.join(grade)

    # 위에꺼나 아래꺼나 뭐 비슷...
    answer = ''
    for i in range(len(scores_arrange)):
        avg_score = sum(scores_arrange[i]) / len(scores_arrange[i]) # 평균 점수 구하기

        if avg_score >= 90:
            answer += 'A'
        elif avg_score >= 80:
            answer += 'B'
        elif avg_score >= 70:
            answer += 'C'
        elif avg_score >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

def solution2(scores):
    answer = ''
    scores_arrange = list(map(list, zip(*scores)))

    for i in range(len(scores_arrange)):

        min_score = min(scores_arrange[i])
        max_score = max(scores_arrange[i])

        cnt = 0
        if min_score == scores_arrange[i][i]:
            cnt = scores_arrange[i].count(min_score)
        elif max_score == scores_arrange[i][i]:
            cnt = scores_arrange[i].count(max_score)

        if cnt == 1:
            avg_score = (sum(scores_arrange[i])-scores_arrange[i][i]) / (len(scores_arrange[i])-1)
        else:
            avg_score = sum(scores_arrange[i]) / len(scores_arrange[i])

        if avg_score >= 90:
            answer += 'A'
        elif avg_score >= 80:
            answer += 'B'
        elif avg_score >= 70:
            answer += 'C'
        elif avg_score >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer



## TEST 1
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores)) # "FBABD"

## TEST 2
scores = [[50,90],[50,87]]
print(solution(scores)) # "DA"

## TEST 3
scores = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(scores)) # "CFD"

