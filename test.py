import time
from collections import deque


start = time.time()
temp = [0 for _ in range(1000000)]
end = time.time()
print(f"{end - start: .5f} sec")


start = time.time()
queue = deque(temp)
end = time.time()
print(f"{end - start: .5f} sec")


start = time.time()
queue = deque([0 for _ in range(1000000)])
end = time.time()
print(f"{end - start: .5f} sec")
