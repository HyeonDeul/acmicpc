n = int(input())

numlist = list(map(int, input().split()))

numlist.sort()

dup = {}

prev = 'a'
cnt = 0

for i in range(n):
    now = numlist[i]
    if prev != now:
        dup[prev] = cnt
        prev = now
        cnt = 0
    else:
        cnt += 1
dup[prev] = cnt

all_num = []

for i in range(n-1):
    for j in range(i+1, n):
        n1 = numlist[i]
        n2 = numlist[j]
        if n1 == 0 and n2 == 0:
            if dup[0] > 2:
                all_num.append(0)
        elif n1 == 0:
            if n2 in dup and dup[n2] > 1:
                all_num.append(n2)
        elif n2 == 0:
            if n1 in dup and dup[n1] > 1:
                all_num.append(n1)
        else:
            all_num.append(n1+n2)
print(all_num)
ans = set(numlist) & set(all_num)
good = len(ans)

for i in dup:
    if i in ans:
        good += dup[i]

print(good)
