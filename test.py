from collections import deque
import copy
import time

a = [1 for _ in range(10000000)]
start = time.time()
b = a[:]
end = time.time()
print(end-start)

start = time.time()
c = copy.deepcopy(a)
end = time.time()
print(end-start)
