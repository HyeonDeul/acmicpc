N = int(input())

t = 1
s = 1
cnt = 1
while s+1 <= abs(N):
    t *= 3
    s += t
    cnt += 1

temp = [0]*cnt

while N < 0:
    if N < 0:
        temp[cnt-1] = -1
    N += 3**(cnt-1)
    cnt -= 1

c = 0
while N != 0:
    temp[c] = N % 3
    N = N//3
    c += 1

l = len(temp)
for i in range(l-1):
    if temp[i] == -1:
        continue
    elif temp[i] == 2:
        temp[i] = -1
        temp[i+1] += 1
    elif temp[i] == 3:
        temp[i] = 0
        temp[i+1] += 1

if temp[l-1] == -1:
    pass
elif temp[l-1] == 2:
    temp[l-1] = -1
    temp.append(1)
elif temp[l-1] == 3:
    temp[l-1] = 0
    temp.append(1)

temp.reverse()
for i in temp:
    if i == -1:
        i = 'T'
    print(i, end='')
