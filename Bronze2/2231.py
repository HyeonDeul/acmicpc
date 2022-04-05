n = int(input())
bs = 0
for i in range(n):
    t = sum(map(int, str(i)))+i
    if t == n:
        bs = i
        break
print(bs)
