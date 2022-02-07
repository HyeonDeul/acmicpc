n = int(input())

numList = list(map(int, input().split()))
numList.sort()


# 중복 수 체크
# 수 개수 -1개
dup = {}
prev = 'a'
cnt = 0

for i in range(n):
    now = numList[i]
    if prev != now:
        dup[prev] = cnt
        prev = now
        cnt = 0
    else:
        cnt += 1
dup[prev] = cnt


numSumList = []

for i in range(n-1):
    for j in range(i+1, n):
        n1 = numList[i]
        n2 = numList[j]
        # 한 수가 0인 경우 모든 수를 만들 수 있지만
        # 다른 수를 만들어야 하므로
        if n1 == 0 and n2 == 0:
            if dup[0] > 1:
                numSumList.append(0)
        elif n1 == 0:
            if n2 in dup and dup[n2] > 0:
                numSumList.append(n2)
        elif n2 == 0:
            if n1 in dup and dup[n1] > 0:
                numSumList.append(n1)
        else:
            numSumList.append(n1+n2)

ans = set(numList) & set(numSumList)
good = len(ans)

for i in dup:
    if i in ans:
        good += dup[i]

print(good)
