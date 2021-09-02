## 사용법 ##

from collections import deque
dq = deque('python')
print(dq)
# deque(['p', 'y', 't', 'h', 'o', 'n'])

# 데이터 삽입
dq.append('x') # 왼쪽에 삽입
print(dq)
# deque(['p', 'y', 't', 'h', 'o', 'n', 'x'])

dq.appendleft('y') # 오른쪽에 삽입
print(dq)
# deque(['y', 'p', 'y', 't', 'h', 'o', 'n', 'x'])

print(dq.pop()) # x
print(dq)
# deque(['y', 'p', 'y', 't', 'h', 'o', 'n'])

print(dq.popleft()) # y
print(dq)
# deque(['p', 'y', 't', 'h', 'o', 'n'])

### 스택으로 사용하려면 --> append / pop ###
