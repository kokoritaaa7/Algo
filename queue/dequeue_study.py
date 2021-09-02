class Node:
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None

    def __str__(self):
        return str(self.data)

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None and self.rear is None:
            return True
        return False

    # 데이터 삽입 - 앞쪽
    def insertFront(self, data):
        new_node = Node(data)

        if self.front is None and self.rear is None:
            self.front = new_node
            self.front.rlink = self.rear
            self.rear = new_node
            self.rear.llink = self.front
        else:
            self.front.llink= new_node # 기존 front의 왼쪽 링크를 새 노드로 변경
            new_node.rlink = self.front # 새 노드의 오른쪽 링크를 기존 front로 변경
            self.front = new_node # front를 새 노드로 변경

    # 데이터 삽입 - 뒤쪽
    def insertRear(self, data):
        new_node = Node(data)

        if self.front is None and self.rear is None:
            self.rear = new_node
            self.rear.llink = self.front
            self.front = new_node
            self.front.rlink = self.rear
        else:
            self.rear.rlink = new_node # 기존 rear의 오른쪽 링크를 새 노드로 변경
            new_node.llink = self.rear # 새 노드의 왼쪽 링크를 기존 rear로 변경
            self.rear = new_node # rear를 새 노드로 변경

    # 데이터 삭제 - 앞쪽
    def deleteFront(self):
        if self.isEmpty():
            return -1
        node = self.front
        if self.rear != self.front:
            self.front = self.front.rlink # 기존 front를 front 오른쪽으로 변경
            self.front.llink = None
        else: # 마지막 일 때
            self.rear = None
            self.front = None

        return node

    # 데이터 삭제 - 뒤쪽
    def deleteRear(self):
        if self.isEmpty():
            return -1

        node = self.rear
        if self.rear != self.front:
            self.rear = self.rear.llink # 기존 rear를 rear 왼쪽으로 변경
            self.rear.rlink = None
        else: # 마지막 일 때
            self.rear = None
            self.front = None

        return node

    def peekFront(self):
        return self.front.data

    def peekRear(self):
        return self.rear.data

    # 출력
    def __str__(self):
        node = self.front
        result = ''
        while node is not None:
            result += str(node) + ' '
            if node == self.rear:
                break
            node = node.rlink
        return result

if __name__ == '__main__':
    deque = Deque()
    deque.insertFront(3)
    deque.insertFront(2)
    deque.insertFront(1)
    print(deque)

    deque.insertRear(4)
    deque.insertRear(5)
    deque.insertRear(6)
    print(deque)

    deque.deleteFront()
    print(deque)
    deque.deleteRear()
    print(deque)

    print('peek front: ', deque.peekFront())
    print('peek rear: ', deque.peekRear())

    while not deque.isEmpty():
        print('delete: ', deque.deleteRear())