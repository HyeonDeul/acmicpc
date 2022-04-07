
n = int(input())
v = 1
for i in range(1, n+1):
    v *= i
r = 0
for i in str(v)[::-1]:
    if i == '0':
        r += 1
    else:
        break
print(r)
