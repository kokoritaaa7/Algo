'''
프로그래머스 - 깊이/너비 우선 탐색(DFS/BFS)
https://programmers.co.kr/learn/courses/30/lessons/43163
단어 변환

2021.10.13
'''

'''
# 접근 방법 #1
1. target이 words에 있는지 확인하고 없으면? return 0
'''

def solution(begin, target, words):
    answer = 0

    # words에 변환할 단어가 없으면 0으로 리턴
    if target not in words:
        return 0

    ## BFS 접근
    visited = []        # 방문한 곳 기록
    queue = [begin]     # 접근할 곳 담기
    while queue:
        check = queue.pop()
        visited.append(check)

        # target이면 끝내기
        if check == target:
            break

        for word in words:
            cnt = 0
            if word in visited: # 이미 방문한 곳이면 pass
                continue

            for idx in range(len(word)):
                if word[idx] != check[idx]:
                    cnt += 1
                if cnt > 2: # 글자가 하나만 달라야되니까
                    break
            if cnt == 1: # 한개만 다르면 접근 가능!
                queue.append(word)

        answer += 1

    return answer



### TEST 1
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words)) # 4


### TEST2
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words)) # 0

