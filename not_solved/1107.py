N = int(input())
M = int(input())

malfunc = []

if M != 0:
    malfunc.extend(list(map(int, input().split())))

nearNumU = N
nearNumD = N

findUpNum = False
findDownNum = False
# 다 고장난 경우 - UP, Down
if len(malfunc) == 10:
    print(abs(N-100))
# 0 빼고 다 고장난 경우 - Up, Down, 0 + Up
elif len(malfunc) == 9 and 0 not in malfunc:
    # 0누르고 방향, 방향
    print(min(N+1, abs(N-100)))
else:
    while True:
        if findUpNum and findDownNum:
            break
        if not findUpNum:
            isMalfunc = False
            for i in str(nearNumU):
                if int(i) in malfunc:
                    isMalfunc = True
                    break
            if not isMalfunc:
                findUpNum = True
            else:
                nearNumU += 1

        if not findDownNum:
            isMalfunc = False
            for i in str(nearNumD):
                if int(i) in malfunc:
                    isMalfunc = True
                    break
            if not isMalfunc:
                findDownNum = True
            else:
                nearNumD -= 1

    UpButton = len(str(nearNumU))+nearNumU-N
    DownButton = len(str(nearNumD))+N-nearNumD
    print(min(UpButton, DownButton, abs(N-100)))
