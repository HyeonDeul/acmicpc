import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    if rock.count(0) == 2:
        cnt = 0
    elif rock.count(0) == 1:
        cnt = 1
    elif rock[0] == 1:
        if rock[1] % 2 == 1 and rock[1] == rock[2]:
            cnt = 1
        else:
            cnt = 0
    elif rock[0] == 2:
        if rock[1] % 2 == 1:
            cnt = 0
        else:
            cnt = 1
    elif rock[0] == 3:
        if rock[1] % 2 == 0 and rock[1] == rock[2]:
            cnt = 1
        else:
            cnt = 0
    elif rock[0] % 2 == 0:
        if rock[0] % 4 == 0:
            cnt = 1 if rock[1] % 2 == 0 else 0
            gap = rock[2]-rock[1]-1
            if gap % 4 == 0 and gap/4 < rock[0]//4:
                cnt = 0 if rock[1] % 2 == 0 else 1
        else:
            cnt = 1 if rock[1] % 2 == 0 else 0
            gap = rock[2]-rock[1]-3
            if gap % 4 == 0 and gap/4 < rock[0]//4:
                cnt = 0 if rock[1] % 2 == 0 else 1
    else:
        cnt = 0
        if (rock[0]-1) % 4 == 0:
            if rock[1] % 2 == 1:
                gap = rock[2]-rock[1]
                if gap % 4 == 0 and gap/4 < rock[0]//4:
                    cnt = 1
            else:
                gap = rock[2]-rock[1]-2
                if gap % 4 == 0 and gap/4 < rock[0]//4:
                    cnt = 1
        else:
            if rock[1] % 2 == 1:
                gap = rock[2]-rock[1]-2
                if gap % 4 == 0 and gap/4 < rock[0]//4:
                    cnt = 1
            else:
                gap = rock[2]-rock[1]
                if gap % 4 == 0 and gap/4 <= rock[0]//4:
                    cnt = 1

    print('B' if cnt == 1 else 'R')
