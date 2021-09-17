'''
프로그래머스 위클리 챌린지
https://programmers.co.kr/learn/courses/30/lessons/86048
7주차

2021.09.14
'''

'''
문제 이해하기
입실 명부 [1, 3, 2]
퇴실 명부 [1, 2, 3]

1은 2번 / 3번 만났을 수도 안만났을 수도 있음
2는 3은 무조건 만남 => 1
3은 2를 무조건 만남 => 1
==> [0, 1, 1]

접근 방법
총 4개의 경우의 수가 존재함
1. 먼저 들어오고 나중에 나간 사람
2. 나중에 들어오고 먼저 나간 사람 > 1 찾을 때 찾아짐 
3. 먼저 들어오고 먼저 나갔지만, 그 사이에 나중에 들어오고 먼저 나간 사람이 있어서 만난게 보장되는 사람

3번을 위해서 set으로 해당 인덱스에 만난 사람을 추가해주는 방식을 해보도록 하자! -> dict key는 사람 번호 value는 set으로 만난 사람들
=> 3번 어케 구하지..ㅠㅠㅠㅠ -> 일단 pass....


접근 방법 2 -> 순서대로
1. 입실시키고 퇴실할 수 있는지 체크
2. 퇴실 할 수 없으면 다음 사람 입실 
3. 퇴실 할 수 있으면 퇴실하고 다음 사람 입실
4. 퇴실하기 전에 해당 배열?에 있는 사람들은 추가해줌 
'''

# enter : 입실 순서
# leave : 퇴실 순서
### 접근 방법 2번 적용 ###
def solution(enter, leave):

    # 만난 사람 저장하는 dict
    meet_people = {idx:set() for idx in enter}

    # room : 회의실에 지금 있는 사람
    room = [enter.pop(0)]

    # 모두가 회의실 다녀갈 때 까지
    while leave:
        # 퇴실해야 되는 사람이 지금 회의실에 있는지 확인
        if leave[0] in room:
            leave_people = leave.pop(0)
            room.remove(leave_people) # 퇴실시키기

        # 퇴실해야 하는 사람이 없으면, 입실 시키기
        else:
            enter_people = enter.pop(0)
            room.append(enter_people) # 입실시키기

            # 새로 들어오면 그 앞에까지 meet_people에 넣어줘야지 -> 같이 회의실에 있다는 것은 만났다는 것이니까
            for i in room[:-1]:
                meet_people[i].add(enter_people)
                meet_people[enter_people].add(i)

    # 배열로 전환
    answer = [0 for _ in range(len(meet_people))]
    for i in meet_people.keys():
        answer[i-1] = len(meet_people[i])

    return answer


### 다른분 풀이 ###
### 참고 : https://blog.naver.com/jjys9047/222504044646 ###
# max_time = (85.38ms, 10.5MB)
### 접근 방법 1과 비슷하게 접근!
def solution2(enter, leave):

    # 이렇게 하면 나중에 배열 따로 안만들어도 되서 효율적일듯
    ans = {idx: 0 for idx in range(1, len(enter) + 1)}
    pre_max = 0 # 일찍 퇴실한 사람들의 입실 기간 중 가장 마지막 시간 확인용
                # => 특정인보다 빨리 퇴실한 사람은 해당 시간보다 빨리 입실할 것
                # => 이를 기준으로 입실 순서를 확인하면 특정인 이후 입실한 사람들 중 pre_max 이전에 입실한 사람은 모두 우리가 원하는 조건을 충족함
                # => 퇴실 시간이 특정 시간 이후지만, 반드시 만나는 것이 확실한 사람이 포함되게 됨
    for i, l in enumerate(leave): # i : 특정인이 퇴실한 시간, l : 특정인
        now = enter.index(l) # 특정인이 입실한 시간
        if i:
            for e in enter[now + 1:pre_max + 1]: # 특정인이 입실한 시간+1 ~ 일찍 퇴실한 사람들의 가장 마지막 시간 => 나중에 들어온 사람 중에 먼저 퇴실한 사람 있는지
                ans[l] += 1
                ans[e] += 1
        pre_max = max(pre_max, now)

    return [v for i, v in ans.items()]


### TEST 1
enter = [1,3,2]
leave = [1,2,3]
print(solution2(enter, leave)) # [0,1,1]

### TEST 2
enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution2(enter, leave)) # [2,2,1,3]

### TEST 3
enter = [3,2,1]
leave = [2,1,3]
print(solution(enter, leave)) # [1,1,2]

### TEST 4
enter = [3,2,1]
leave = [1,3,2]
print(solution(enter, leave)) # [2,2,2]

### TEST 5
enter = [1,4,2,3]
leave = [2,1,4,3]
print(solution(enter, leave)) # [2,2,0,2]

