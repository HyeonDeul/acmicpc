arr = []
for _ in range(int(input())):
    t = int(input())
    if t == 0:
        arr.pop()
    else:
        arr.append(t)
print(sum(arr))
