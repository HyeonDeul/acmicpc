import sys


def game(rock, now):
    if rock.count(0) > 1:
        return rock, now
    else:

        rock.sort()
        if rock[0] == 0:
            winRock, winner = game([0, rock[1]-1, rock[2]-1], -1*now)
            return winRock, winner
        else:
            rockList = [[rock[0]-1, rock[1]-1, rock[2]],
                        [rock[0]-1, rock[1], rock[2]-1],
                        [rock[0], rock[1]-1, rock[2]-1]]
            for i in range(3):
                winRock, winner = game(rockList[i], -1*now)
                if winner == now:
                    winRock = rockList[i]
                    break
            return winRock, winner


while True:
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    now = 1

    while True:
        rock, winner = game(rock, now)
        print(rock, '나는', now, '이고, 승자는', winner)
        if winner != now:
            break
        if rock.count(0) == 2:
            break
        now *= -1

    print('R' if winner == 1 else 'B')
