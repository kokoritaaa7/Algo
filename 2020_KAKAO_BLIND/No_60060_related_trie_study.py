'''
프로그래머스 2020 KAKAO BLIND
https://programmers.co.kr/learn/courses/30/lessons/60060
가사 검색에서 사용된 Trie 자료구조

2021.09.07
'''

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # 문자열의 종료를 알리는 flag
        self.children = {} # 자식 노드를 저장

class Trie:
    def __init__(self):
        self.head = Node(None)

    # 입력된 문자열을 하나씩 children에 확인 후 저장하고, 문자열을 다 돌면 마지막 노드의 data에 문자열을 저장
    def insert(self, string):
        '''string을 추가하는 함수'''
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)

            current_node = current_node.children[char]
        current_node.data = string

    # 마지막 노드가 data에 존재한다면 True, 존재하지 않는다면 False
    def search(self, string):
        '''문자열 존재 여부 리턴'''
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    # prefix로 시작하는 단어가 존재한다면 해당 단어 배열로 return
    def starts_with(self, prefix):
        '''prefix로 시작하는 단어 찾기'''
        current_node = self.head
        words = []
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))

            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


### TEST ###
trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)

print(trie.search("friend"))    # False
print(trie.search("frodo"))     # True
print(trie.search("fire"))      # True
print(trie.starts_with("fire")) #['fire', 'firefox']