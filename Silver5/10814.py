n = int(input())
a = []
for _ in range(n):
    x, y = map(str, input().split())
    a.append([int(x), y])
a.sort(key=lambda x: x[0])
for i in a:
    print(*i)
