'''
프로그래머스 위클리 챌린지
https://programmers.co.kr/learn/courses/30/lessons/84325
4주차

2021.09.03
'''

def solution(table, languages, preference):
    new_table = {}
    for t in table:
        temp = t.split()
        new_table[temp[0]] = temp[1:]

    # print(new_table)
    #
    # job = []
    # job_dict = {}
    # for t in table:
    #     temp = ''
    #     for i, d in enumerate(t.split()):
    #         if i == 0:
    #             job.append(d)
    #             job_dict[d] = {}
    #             temp = d
    #         else:
    #             job_dict[temp][d] = 6 - i

    result = {}
    for i in range(len(languages)):
        for k, v in new_table.items():
            if languages[i] in v:
                calc = (5 - v.index(languages[i])) * preference[i]
                try:
                    result[k] += calc
                except:
                    result[k] = calc

    answer = ''
    max_data = 0
    for k, v in result.items():
        if v > max_data:
            answer = k
            max_data = v
        elif v == max_data:
            answer = min(k, answer)


    return answer



### TEST 1
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
language = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, language, preference)) # Hardware

### TEST 2
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
language = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, language, preference)) # Portal