import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    cnt = 0

    if rock.count(1) == 3:
        cnt = 1
    elif rock[0] == 1:
        if rock[1] == rock[2] and rock[1] % 2 == 1:
            cnt = 1
        else:
            cnt = 0
    elif rock.count(1) > 0:
        cnt = 0

    # 홀수
    elif rock[0] % 2 == 1:
        # 홀수 홀수
        if rock[1] % 2 == 1:
            if rock[0] == 3:
                cnt = 0
            # 둘이 같은경우ㄴ
            elif rock[0] == 5:
                if rock[1] == rock[2]:
                    cnt = 1
                else:
                    cnt = 0
            elif (rock[0]-1) % 4 == 0:
                if rock[1] == rock[2]:
                    cnt = 1
                elif rock[1]+4 == rock[2]:
                    cnt = 1
                else:
                    cnt = 0
            else:
                if rock[1]+2 == rock[2]:
                    cnt = 1
                else:
                    cnt = 0
        # 홀수 짝수
        else:
            if rock[0] == 3:
                if rock[1] == rock[2]:
                    cnt = 1
                else:
                    cnt = 0
            # 홀 짞 짝
            elif rock[2] % 2 == 0:
                # [0]이 4의 배수인경우
                if (rock[0]-1) % 4 == 0:
                    if rock[1]+2 == rock[2]:
                        cnt = 1
                    else:
                        cnt = 0
                # [0]이 4의 배수가 아닌경우
                else:
                    if (rock[2]-rock[1]) % 4 == 0:
                        cnt = 1
                    else:
                        cnt = 0
            # 홀 짞 홀
            else:
                cnt = 0

    # 짝수
    else:
        if rock[0] == 2:
            if rock[1] % 2 == 0:
                cnt = 1
            else:
                cnt = 0
        # [0] 4의 배수
        elif rock[0] % 4 == 0:
            # [1] 짝수
            if rock[1] % 2 == 0:
                if rock[1]+1 == rock[2]:
                    cnt = 0
                else:
                    cnt = 1
            else:
                if rock[1]+1 == rock[2]:
                    cnt = 1
                else:
                    cnt = 0
        # [0] 4의 안 배수
        else:
            if rock[1] % 2 == 0:
                if rock[1]+3 == rock[2]:
                    cnt = 0
                else:
                    cnt = 1
            else:
                if rock[1]+3 == rock[2]:
                    cnt = 1
                else:
                    cnt = 0

    print('B' if cnt % 2 == 1 else 'R')
