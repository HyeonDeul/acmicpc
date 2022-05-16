import time
from collections import deque


b = deque()
start = time.time()
for i in range(100000):
    b.appendleft(i)
end = time.time()
print(end - start)

a = []
start = time.time()
for i in range(100000):
    a.insert(0, i)
end = time.time()
print(end - start)
