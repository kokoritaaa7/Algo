class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedListQueue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        dequeueObj = None
        if self.isEmpty():
            return -1
        else:
            dequeueObj = self.front.data
            self.front = self.front.next

        if self.front is None:
            self.rear = None

        return dequeueObj

    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.front.data

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def __str__(self):
        node = self.front
        result = ''
        while node is not None:
            result += str(node) + ' '
            if node == self.rear:
                break
            node = node.next

        return result

if __name__ == "__main__":
    m_queue = LinkedListQueue()
    m_queue.enqueue(1)
    print(m_queue)
    m_queue.enqueue(2)
    print(m_queue)
    m_queue.enqueue(3)
    print(m_queue)
    print('dequeue: ', m_queue.dequeue())
    print('peek: ', m_queue.peek())
    while not m_queue.isEmpty():
        print('dequeue: ', m_queue.dequeue())