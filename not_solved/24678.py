import math
import sys

# for _ in range(int(input())):
#     rock = list(map(int, sys.stdin.readline().split()))
#     rock.sort()

#     cnt = 0
#     while True:
#         # print(rock)
#         if rock[0] == rock[1] == rock[2]:
#             cnt += 3*(rock[0]-1)+1
#             print('B' if cnt % 2 == 1 else 'R')
#             break
#         else:
#             if rock[1] != rock[0]:
#                 gap = math.ceil((rock[1]-rock[0])/2)
#             else:
#                 gap = math.ceil((rock[2]-rock[0])/2)

#             if rock.count(0) == 2:
#                 print('B' if cnt % 2 == 1 else 'R')
#                 break
#             cnt += gap
#             rock[0] += gap
#             rock[1] -= gap
#             rock[2] -= gap
#             rock.sort()

rock = list(map(int, sys.stdin.readline().split()))
rock.sort()

cnt = 0
while True:
    # print(rock)
    if rock[0] == rock[1] == rock[2]:
        cnt += 3*(rock[0]-1)+1
        print('B' if cnt % 2 == 1 else 'R')
        break
    else:
        if rock[1] != rock[0]:
            gap = math.ceil((rock[1]-rock[0])/2)
        else:
            gap = math.ceil((rock[2]-rock[0])/2)

        if rock.count(0) == 2:
            # print('B' if cnt % 2 == 1 else 'R')
            print(cnt)
            break
        cnt += gap
        rock[0] += gap
        rock[1] -= gap
        rock[2] -= gap
        rock.sort()
