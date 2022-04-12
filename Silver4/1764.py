import sys
n, m = map(int, sys.stdin.readline().split())
d = set()
b = set()
for _ in range(n):
    d.add(sys.stdin.readline().rstrip())
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())
a = list(d & b)
a.sort()
print(len(a))
for i in a:
    print(i)
