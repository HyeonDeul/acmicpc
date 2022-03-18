import sys

rock = list(map(int, sys.stdin.readline().split()))
rock.sort()

# 1=R, -1=B
winner = 1

cnt = 0
while True:
    cnt += 1
    if rock.count(0) > 1:
        break
    if rock[0] == 1:
        rock[0] -= 1
        if rock[1] % 2 == 1:
            rock[2] -= 1
        else:
            rock[1] -= 1
    elif rock[0] % 2 == 1:
        rock[0] -= 1
        rock[2] -= 1
    else:
        rock[1] -= 1
        rock[2] -= 1

    rock.sort()
    winner *= -1
print('R' if winner == 1 else 'B')
