class Queue:
    def __init__(self):
        self.data = list()

    # 데이터 삽입
    def enqueue(self, value):
        self.data.append(value)

    # 데이터 삭제
    def dequeue(self):
        if not self.empty():
            return self.data.pop(0)
        else:
            return -1

    # 맨 앞 원소(= front) 확인
    def peek(self):
        return self.data[0]

    # 비어있는지 확인
    def empty(self):
        if not self.data:
            return True
        else:
            return False


### TEST ###
if __name__ == '__main__':
    # 스택 인스턴스 생성
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.peek()

    while not q.empty():
        print(q.dequeue(), end=" ")
