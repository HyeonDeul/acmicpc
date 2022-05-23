from collections import deque
import time

a = []
start = time.time()
for i in range(10000000):
    a.append(i)
for _ in range(10000000):
    a.pop()
end = time.time()
print(end-start)

b = deque()
start = time.time()
for i in range(10000000):
    b.append(i)
for _ in range(10000000):
    b.pop()
end = time.time()
print(end-start)
