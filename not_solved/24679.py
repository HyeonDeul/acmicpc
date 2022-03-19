import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    cnt = 0

    if rock.count(1) == 3:
        cnt = 1
    elif rock.count(1) > 0:
        cnt = 0
    else:
        if rock[0] % 2 == 1:
            cnt += 1
            rock[0] -= 1
            rock[1] -= 1
        rock.sort()

        gap = rock[1]-rock[0]
        cnt += gap
        rock[1] -= gap
        rock[2] -= gap

        # 차이보다 2로가는게 더 빠르다면
        if 2*(rock[0]-2) <= rock[2]-2:
            cnt += 1
        # 2로가는 것보다 차이좁혀지는게 더 빠르다면
        else:
            if rock[2] % 2 == 0:
                # 짝추 차이 좁아지는건 짝수
                # 즉 3의 배수로 2가 되는게 중요
                # cnt += ((2*rock[0]-rock[2])-2)//2*3+1
                if ((2*rock[0]-rock[2])-2) % 4 != 0:
                    cnt += 1
            else:
                if ((2*rock[0]-rock[2]+1)-2) % 4 != 0:
                    cnt += 1
                # cnt += ((2*rock[0]-rock[2]+1)-2)//2*3+1

    print('B' if cnt % 2 == 1 else 'R')

# 2 2 를 가진 사람이 짐 -> 2 2을 만들어 줘야함
