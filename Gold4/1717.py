n, m = map(int, input().split())
setlist = []
for _ in range(m):
    c, a, b = map(str, input().split())
    if c == '0':
        idxa, idxb = -1, -1
        for i in range(len(setlist)):
            if a in setlist[i]:
                idxa = i
            if b in setlist[i]:
                idxb = i
            if idxa != -1 and idxb != -1:
                break

        if idxa == -1 and idxb == -1:
            setlist.append(a+b)
        elif idxa != idxb:
            setlist[idxa] += setlist[idxb]
            setlist.pop(idxb)
        elif idxa == -1:
            setlist[idxb] += a
        elif idxb == -1:
            setlist[idxa] += b
    else:
        same = False
        for i in setlist:
            if a in i:
                if b in i:
                    same = True
                break
            if b in i:
                if a in i:
                    same = True
                break

        print("YES" if same else "NO")
