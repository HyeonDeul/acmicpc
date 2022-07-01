import sys
input = sys.stdin.readline

N = int(input())
assem = []
alpha = [0 for _ in range(27)]
for _ in range(N):
    assem.append(input().rstrip())

assem.sort()

prev = 'a'
for i in range(N):
    a = assem[i][0]
    if a != prev:
        alpha[ord(a[0])-6] = i
        prev = a

K = int(input())
for _ in range(K):
    mal = input().rstrip()
    l = len(mal)
    idx = ord(mal[0])-65
    start = alpha[idx]
    end = alpha[idx+1]
    if start == -1:
        print(0)
        continue
    if end == -1:
        end = N
    longStr = ''
    longCnt = -1
    tempStr = ''
    tempCnt = 0

    for i in range(start, end):
        now = assem[i]
        if mal == now[:l]:
            if now == tempStr:
                tempCnt += 1
            else:
                if longCnt < tempCnt:
                    longCnt = tempCnt
                    longStr = tempStr
                tempStr = now
                tempCnt = 1
        if longCnt < tempCnt:
            longCnt = tempCnt
            longStr = tempStr

    if longCnt == -1:
        print(0)
    else:
        print(longStr, longCnt)
