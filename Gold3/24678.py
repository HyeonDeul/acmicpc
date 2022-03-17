import sys

for _ in range(int(input())):
    rock = list(map(int, sys.stdin.readline().split()))
    rock.sort()

    cnt = 0

    gap = (rock[1]-rock[0])//2
    cnt += gap
    rock[0] += gap
    rock[1] -= gap
    rock[2] -= gap
    gap = 2*((rock[2]-rock[0])//2)
    cnt += gap
    rock[2] -= gap

    toOne = rock[0]-1
    cnt += 3*toOne
    rock[0] -= toOne
    rock[1] -= toOne
    rock[2] -= toOne
    rock.sort()
    if rock == [1, 1, 1]:
        cnt += 1
    elif rock == [1, 1, 2]:
        cnt += 3
    elif rock == [1, 2, 2]:
        cnt += 4

    print('B' if cnt % 2 == 1 else 'R')
