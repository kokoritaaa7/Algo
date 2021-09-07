'''
프로그래머스 2020 KAKAO BLIND
https://programmers.co.kr/learn/courses/30/lessons/60059
가사 검색

2021.09.07
'''

'''
문제 이해하기
queries에 있는 단어가 words에 있는지 파악해야 함
- 글자 수 다르면 매치되지 않음 -> 매치되지 않음은 0으로 표기
- 검색 키워드는 ?로 표기 

접근 방법 -> 1차
1. query와 word 단어가 같은지 확인 
2. 같으면 3번 진행 다르면 다음 query로 넘어감
3. query에서 물음표가 아닌 문자열의 인덱스를 뽑아내고
4. 해당 인덱스에 있는 query와 word가 같은지 확인
5. 다르면 다음 query로 넘어감  

2차 -> 추가로 생각하기
- 모든 단어가 다 ?일 때
====> 실패 

3차 -> Trie 알고리즘 사용하기 
'''

### 3차 코드 ###
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.count = 0
        self.data = data # 문자열의 종료를 알리는 flag
        self.children = {} # 자식 노드를 저장
        

class Trie:
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    # 입력된 문자열을 하나씩 children에 확인 후 저장하고, 문자열을 다 돌면 마지막 노드의 data에 문자열을 저장
    def insert(self, string):
        '''string을 추가하는 함수'''
        current_node = self.head
        self.count += 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)

            current_node = current_node.children[char]
            current_node.count += 1

        current_node.data = string

    # prefix로 시작하는 단어가 존재한다면 해당 단어 배열로 return
    def starts_with(self, prefix):
        '''prefix로 시작하는 단어 찾기'''
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        return current_node.count

def solution(words, queries):
    answer = []
    prefix = {}
    suffix = {}

    # 글자 길이에 따라 만들어주기
    for word in words:
        if len(word) not in prefix:
            prefix[len(word)] = Trie()
            suffix[len(word)] = Trie()
        
        prefix[len(word)].insert(word)
        suffix[len(word)].insert(word[::-1])

    # 같은 글자수 없으면 바로 다음 쿼리로 넘어가기
    for query in queries:
        if len(query) not in prefix:
            answer.append(0)
            continue
        
        # 접미사
        if query[0] == '?':
            if query[-1] == '?':
                answer.append(prefix[len(query)].count)
                continue

            idx = query.count('?')
            sp = query[idx:][::-1]
            answer.append(suffix[len(query)].starts_with(sp))
        else: # 접두사
            idx = query.count('?')
            sp = query[:len(query) - idx]
            answer.append(prefix[len(query)].starts_with(sp))
    
    return answer   


### 참고한 코드 ###
# class Node(object):
#     def __init__(self, key):
#         self.key = key
#         self.count = 0
#         self.terminal = False
#         self.children = {}
#
#     def get_key(self):
#         return self.key
#
#
# class Trie:
#     def __init__(self):
#         self.head = Node(None)
#         self.count = 0
#
#     def insert(self, string):
#         current_node = self.head
#         self.count += 1
#
#         for char in string:
#             if char not in current_node.children:
#                 current_node.children[char] = Node(char)
#             current_node = current_node.children[char]
#             current_node.count += 1
#
#         current_node.terminal = True
#
#     def search(self, string):
#         current_node = self.head
#
#         for char in string:
#             if char in current_node.children:
#                 current_node = current_node.children[char]
#             else:
#                 return False
#
#         return current_node.terminal
#
#     def starts_with(self, prefix, wildcard):
#         current_node = self.head
#
#         for p in prefix:
#             if p in current_node.children:
#                 current_node = current_node.children[p]
#             else:
#                 return 0
#
#         return current_node.count
#
#
# def solution(words, queries):
#     answer = []
#     front_trie = {}
#     back_trie = {}
#
#     # 글자 길이 수에 따라 trie을 각각 만들어 준다
#     # ???갯수에 따라 탐색을 계속 할 필요 없도록 하기 위함이다
#     for word in words:
#         if len(word) not in front_trie:
#             front_trie[len(word)] = Trie()
#             back_trie[len(word)] = Trie()
#
#         front_trie[len(word)].insert(word)
#         back_trie[len(word)].insert(word[::-1])
#
#     for query in queries:
#         if len(query) not in front_trie:
#             answer.append(0)
#             continue
#
#         # 전부 물음표인 경우
#         if len(query) == query.count('?'):
#             answer.append(front_trie[len(query)].count)
#             continue
#
#         if query[-1] == '?':
#             w = query.count('?')
#             p = query[:len(query) - w]
#             answer.append(front_trie[len(query)].starts_with(p, w))
#         else:
#             w = query.count('?')
#             p = query[w:][::-1]
#             answer.append(back_trie[len(query)].starts_with(p, w))
#     return answer
#


### TEST 1
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries)) # [3, 2, 4, 1, 0]

### TEST 2
words = ['abcd', 'eeee', 'hell', 'ieis', 'dksl']
queries = ['????']
print(solution(words, queries)) # [5]


# ## 시간초과 - 1, 2차 ###
# def solution(words, queries):
#     answer = []
#
#     for query in queries:
#         temp = [word for word in words if len(word) == len(query)] # 글자수 같은 것만 일단 뽑기
#         # print(temp)
#
#         # 같은 글자수 없으면 바로 다음 쿼리로 넘어가기
#         if not temp:
#             answer.append(0)
#             continue
#
#         cnt = 0
#         if query[0] == '?': # 키워드가 접미사일 때
#             if query[-1] == '?':
#                 answer.append(len(temp))
#                 continue
#
#             idx = query[::-1].index('?') # O(N)
#             sp = query[len(query)-idx:] # O(1)
#             for t in temp:
#                 if t.endswith(sp):
#                     cnt += 1
#         else:   # 키워드가 접두사일 때
#             # sp = query.split('?')[0]
#             idx = query.index('?')
#             sp = query[:idx]
#             print(sp)
#             for t in temp:
#                 if t.startswith(sp):
#                     cnt += 1
#
#         answer.append(cnt)
#
#     return answer