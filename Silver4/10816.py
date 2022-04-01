n = int(input())
cards = list(map(int, input().split()))
cards.sort()
c = {}
for i in cards:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

m = int(input())
s = []
targets = list(map(int, input().split()))
for t in targets:
    if t in c:
        s.append(c[t])
    else:
        s.append(0)

print(*s)
