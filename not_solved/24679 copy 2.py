import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    cnt = 0
    # 홀수
    if rock[0] % 2 == 1:
        # 홀수
        if rock[1] % 2 == 1:
            if ((rock[0]-1)/2) % 2 == 0 and rock[1] == rock[2]:
                cnt = 1
            else:
                cnt = 0
        # 짝수
        else:
            if ((rock[0]-1)/2) % 2 == 1 and rock[1] == rock[2]:
                cnt = 1
            else:
                cnt = 0

    # 짝수
    else:
        if (rock[0]/2+rock[1]) % 2 == 0:
            cnt = 0
        else:
            cnt = 1

    print('B' if cnt % 2 == 1 else 'R')
