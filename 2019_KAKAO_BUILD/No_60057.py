'''
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/60057
2020 KAKAO BLIND RECRUITMENT - 문자열 압축

2021.09.05
'''

'''
일단 접근 방식 -> 최소값 : len(s)로 두고, 나머지랑 비교하기
나머지란 => 2~len(s)/2 개 까지 조사하면서 순서대로 비교 
'''

def solution(s):
    result = len(s)

    for step in range(1, len(s)//2+1): # 쪼개지는 데이터는 1부터 len(s)//2 + 1까지 (이유 : 1/2보다 크면 2개로 쪼개질수조차 없어서)
        lastStr = ''    # 이전 단어 저장하는 변수
        i = step        # 간격 계속 더하기 위한 변수
        st = 0          # 인덱스 시작 변수
        arr = []        # 길이 구하기 위한 배열

        while i <= len(s):
            if s[st:i] == lastStr:          # 이전 단어랑 같으면
                if type(arr[-1]) == int:    # 숫자면 -> 이미 숫자가 있다는 뜻이니까 +1
                    arr[-1] += 1
                else:                       # 문자면 -> 숫자는 처음이니까 2를 넣어줌 (2개 겹치는게 기본이니까 바로 2부터)
                    arr.append(2)
            else:                           # 이전 단어랑 다르면
                arr.append(s[st:i])         # 배열에 해당 문자 넣어주고
                lastStr = arr[-1]           # 현재 단어를 이전 단어 변수에 넣어주기

            st, i = i, i + step             # 글자 자르기 위해서 st, i를 변경해줌

        new_result = ''.join(list(map(str,arr))) + s[st:]   # 배열 값 string으로 변환 (len알기위해서)
        # print(new_result)
        result = min(result, len(new_result))   # 최소값 저장

    return result


### TEST 1
s = "aabbaccc" # 2a2ba3c
print(solution(s))

### TEST 2
s = "ababcdcdababcdcd" #
print(solution(s))

### TEST 3
s = "abcabcdede" #
print(solution(s))

### TEST 4
s = "abcabcabcabcdededededede" # 2abcabc2dedede (6개)
print(solution(s))

### TEST 5
s = "xababcdcdababcdcd"
print(solution(s))