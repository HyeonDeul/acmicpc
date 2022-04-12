import sys

for _ in range(int(sys.stdin.readline())):
    queue = []
    l = 0
    for _ in range(int(sys.stdin.readline())):
        c, n = map(str, sys.stdin.readline().rstrip().split())
        n = int(n)
        if c == 'I':
            ins = False
            if l == 0:
                queue.append(n)
            elif queue[l-1] <= n:
                queue.append(n)
            elif queue[0] >= n:
                queue.insert(0, n)
            else:
                upidx = l
                doidx = 0
                while upidx != doidx+1:
                    mididx = (upidx+doidx)//2
                    if n > queue[mididx]:
                        doidx = mididx
                    elif n == queue[mididx]:
                        upidx = mididx
                    else:
                        upidx = mididx
                queue.insert(upidx, n)
            l += 1
        else:
            if l != 0:
                l -= 1
                if n == 1:
                    queue.pop()
                else:
                    queue.pop(0)
    if l == 0:
        print("EMPTY")
    else:
        print(queue[l-1], queue[0])
