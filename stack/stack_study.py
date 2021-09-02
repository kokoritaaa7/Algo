# 스택에 필요한 기능이 이미 파이썬 리스트에 구현되어 있음

class Stack:
    def __init__(self):
        self.data = list()

    # 데이터 삽입
    def push(self, value):
        self.data.append(value)

    # 데이터 삭제
    def pop(self):
        if self.is_empty():
            # 언더플로우 예외 처리
            # 데이터 없을 때 삭제하면 에러 발생하니까
            return
        else:
            return self.data.pop(-1)  # 리스트 자체 함수 사용

    # 마지막 원소(= top) 확인
    def peek(self):
        if self.is_empty():
            # 언더플로우 예외 처리
            return
        else:
            last_index = len(self.data) - 1
            return self.data[last_index]

    # 비어있는지 확인
    def is_empty(self):
        # self.data 가 있으면 True니까 empty가 아니므로 not 붙어서 False 리턴
        return not self.data


### TEST ###
if __name__ == '__main__':
    # 스택 인스턴스 생성
    stack = Stack()
    print(stack.peek())

    # 데이터 삽입
    stack.push(1)
    print(stack.peek())
    stack.push(2)
    print(stack.peek())
    stack.push(3)
    print(stack.peek())
    stack.push(4)
    print(stack.peek())

    # 데이터 삭제
    stack.pop()
    print(stack.peek())

    # 비었는지 확인
    print(stack.is_empty())

    # 남은 요소 제거하며 출력
    while not stack.is_empty():
        print(stack.pop())