'''
프로그래머스 [해시]
https://programmers.co.kr/learn/courses/30/lessons/42579
베스트 앨범

2021.09.12
'''

'''
문제 이해하기

노래 수록 기준
1. 많이 재생된 장르
2. 장르내에서 많이 재생된 곡 
3. 재생횟수 같으면? -> 고유번호 낮은 순
** 장르별로 2개씩만 뽑음

접근 방식
1. 장르별 총 노래 재생 횟수 구하기 + 결과값에 필요한 데이터 하나의 dict으로 만들기
2. 장르별 총 노래 재생 횟수가 큰 순서대로 정렬
3. 2번에서 큰 순서대로 각 노래별 재생 횟수 큰 순서대로 정렬하고 2개 짜르기
'''

def solution(genres, plays):
    answer = []

    total = {} # 장르별 총 재생 횟수 => {장르:총 재생 횟수}
    album = {} # {장르:[(인덱스, 노래횟수)]}
    for idx, li in enumerate(zip(genres,plays)):
        total.setdefault(li[0], 0)
        total[li[0]] += li[1]

        album.setdefault(li[0], [])
        album[li[0]].append((idx, li[1]))

    # 장르별 재생 횟수 큰 순서대로
    seq = sorted(total, key=lambda x: total[x], reverse=True)

    for s in seq:
        # 장르 내에서 노래 재생 횟수 큰 순서대로 (인덱스, 노래 재생 횟수)
        b = sorted(album[s], key=lambda x: x[1], reverse=True)
        for idx, count in b[:2]: # 장르별 최대 2개까지니까
            answer.append(idx)

    return answer

### TEST 1
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays)) # [4, 1, 3, 0]

# ### TEST 2
genres = ["classic", "pop", "classic", "classic", "pop", "classic", "hiphop"]
plays = [500, 600, 150, 800, 2500, 3000, 1]
print(solution(genres, plays)) # [5, 3, 4, 1, 6]