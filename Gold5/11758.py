x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def Leftside(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])


# slope1 = y1-y2 / x1-x2
# slope2 = y2-y3 / x2-x3

# up = 1, down = -1

if y3-y2 > 0:
    dir = 1
if y3-y2 == 0:
    if x3-x2 > 0:
        dir = 1
    else:
        dir = -1
else:
    dir = -1


# if slope1 == slope2:
#     answer = 0
# else:
#     side = Leftside([x2, y2], [x3, y3], [x1, y1])

#     if dir*side < 0:
#         answer = 1
#     else:
#         answer = -1
# print(answer)

side = Leftside([x2, y2], [x3, y3], [x1, y1])

if dir*side < 0:
    answer = 1
elif dir*side == 0:
    answer = 0
else:
    answer = -1
print(answer)
