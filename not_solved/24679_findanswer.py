import sys


def game(rock, now, rock_list=[]):
    if rock.count(0) > 1:
        return rock, now, rock_list
    else:
        rock.sort()
        if rock[0] == 0:
            rock_list.append([0, rock[1]-1, rock[2]-1])
            winRock, winner, seque = game(
                [0, rock[1]-1, rock[2]-1], -1*now, rock_list)
            return winRock, winner, seque
        else:
            rockList = [[rock[0]-1, rock[1]-1, rock[2]],
                        [rock[0]-1, rock[1], rock[2]-1],
                        [rock[0], rock[1]-1, rock[2]-1]]
            for i in range(3):
                temp = rock_list[:]
                temp.append(rockList[i])
                winRock, winner, seque = game(rockList[i], -1*now, temp)
                winRock = rockList[i]
                if winner == now:
                    break

            return winRock, winner, seque


while True:
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    now = 1

    while True:
        rock, winner, RockList = game(rock, now, [rock])
        if winner != now:
            break
        now *= -1
    print(RockList)
    print('R' if winner == 1 else 'B')
