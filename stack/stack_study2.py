class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None

    # 데이터 삽입
    def push(self, value):
        new_node = Node(value)
        new_node.prev = self.head
        self.head = new_node

    # 데이터 삭제
    def pop(self):
        if self.is_empty():
            # 언더플로우 예외 처리
            return
        else:
            value = self.head.data
            self.head = self.head.prev
            return value

    # 마지막 원소 확인
    def peek(self):
        if self.is_empty():
            # 언더플로우 예외 처리
            return
        else:
            return self.head.data

    # 비어있는지 확인
    def is_empty(self):
        return not self.head

if __name__ == '__main__':
    # 스택 인스턴스 생성
    stack = Stack()
    print(stack.peek()) # None

    # 데이터 삽입
    stack.push(1)
    print(stack.peek()) # 1
    stack.push(2)
    print(stack.peek()) # 2
    stack.push(3)
    print(stack.peek()) # 3
    stack.push(4)
    print(stack.peek()) # 4

    # 데이터 삭제
    stack.pop()
    print(stack.peek()) # 3

    # 비어있는지 확인
    print(stack.is_empty()) # False

    # 남은 요소 제거하며 출력
    while not stack.is_empty():
        print(stack.pop())
        '''
        3
        2
        1
        '''