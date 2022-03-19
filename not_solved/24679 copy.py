import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    cnt = 0

    if rock.count(1) == 3:
        cnt = 1
    elif rock.count(1) > 0:
        cnt = 0
    # 홀수
    elif rock[0] % 2 == 1:
        if rock[1] == rock[2] and rock[1] % 2 == 1:
            cnt = 1
        else:
            cnt = 0
    # 짝수
    else:
        # 홀수
        if rock[1] % 2 == 1:
            cnt = 0
        # 짝수
        else:
            if (rock[0]/2) % 2 == 1:
                cnt = 1
            else:
                cnt = 0

    print('B' if cnt % 2 == 1 else 'R')
