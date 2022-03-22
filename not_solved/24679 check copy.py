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
                winRock = rockList[i]
                if winner == now:
                    break
            return winRock, winner


dif = []
with open("test.txt", 'w') as f:
    f.write('\t\t\t\t\tMy code \tAlgorithm\n')

    for i in range(1, 15):
        for j in range(i, 15):
            for k in range(j, 15):

                rock = [i, j, k]
                rock.sort()

                rockList = [[rock[0]-1, rock[1]-1, rock[2]],
                            [rock[0]-1, rock[1], rock[2]-1],
                            [rock[0], rock[1]-1, rock[2]-1]]
                for now in range(3):
                    rock = rockList[now]
                    rock.sort()
                    if rock.count(0) > 1:
                        cnt = 0
                    elif rock.count(0) == 1:
                        cnt = 1
                    elif rock.count(1) == 3:
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
                            # 둘이 같은경우
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
                                    # if (rock[2]-rock[1]) % 4 == 0:
                                    if rock[1]+2 == rock[2]:
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
                        elif rock[2]-rock[1] == 5 and rock[0] != 4 and rock[0] != 6:
                            if rock[0] % 4 == 0:
                                cnt = 0
                            else:
                                cnt = 1
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
                        if cnt == 1:
                            break

                winner1 = 'B' if cnt == 0 else 'R'

                line = '[ '+str(i)+' '+str(j)+' '+str(k)+' ]\twin :\t'+winner1

                # 알고리즘
                rock = [i, j, k]
                orinRock = [i, j, k]
                rock.sort()

                now = 1

                while True:
                    rock, winner = game(rock, now)
                    if winner != now:
                        break
                    if rock.count(0) == 2:
                        break
                    now *= -1

                winner2 = 'R' if winner == 1 else 'B'
                line += '\t\t\t'+winner2+'\n'
                f.write(line)

                if winner1 != winner2:
                    dif.append(orinRock)

    f.write('\ndifferent list\n')
    for rock in dif:
        line = '[ '
        for j in rock:
            line += str(j)+' '
        line += ']'
        f.write(line+'\n')
