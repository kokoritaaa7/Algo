'''
프로그래머스 - 깊이/너비 우선 탐색(DFS/BFS)
https://programmers.co.kr/learn/courses/30/lessons/43162
네트워크

2021.10.10
'''

'''
접근 방법 # 1
n - 연결된 숫자 => 정답아닌가?
=> (1, 2)나 (2, 1) 은 1개 연결이니까 이 부분은 어떻게 처리하지
=> (n,n)전까지만 가보는 것! => (실패) 이유: n=6일때, 1,2,3 모두 연결 5,6 연결이면 연결된 개수는 4개 인데 그룹은 3개가 나와야하니까

접근 방법 # 2 
2차원 배열에서 탐색하면서 (n,n) 제외 하고 값이 1인 것 만나면 그 행으로 이동 
그 행에서 값이 1인 또 다른 좌표를 구하기

 

'''

# 접근방법: n - 연결된 숫자
# def solution(n, computers):
#     answer = 0
#
#     for i in range(n):
#         # 중복되니까 (n, n)전까지만 접근하기
#         for j in range(0, i):
#             if computers[i][j] == 1:
#                 answer += 1
#     return n - answer

def solution(n, computers):
    answer = []
    visited = [False for _ in range(n)]
    cnt = 0

    for v in range(n):
        if visited[v]:
            continue
        else:
            answer.append(v)

        while answer:
            r = answer.pop(0)
            visited[r] = True
            for i in range(n):
                if computers[r][i] == 1 and not visited[i]:
                    answer.append(i)
        cnt += 1

    return cnt


### TEST 1
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers)) # 2

### TEST 2
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers)) # 1

### TEST 3
n = 6
computers = [[1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]
print(solution(n, computers))