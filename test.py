from collections import deque
import copy
import time

a = [1 for _ in range(100000)]
start = time.time()
for _ in range(100000):
    b = a[0]
    del a[0]
end = time.time()
print(end-start)

a = [1 for _ in range(100000)]
start = time.time()
for _ in range(100000):
    b = a.pop()
end = time.time()
print(end-start)
