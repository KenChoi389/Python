from collections import deque

queue=deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.append(4)
print(queue.popleft())
# print(queue)
# print(queue[0])
# queue.reverse()
# print(queue)
