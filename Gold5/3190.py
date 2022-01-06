import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = []
for i in range(K):
    row, col = map(int, sys.stdin.readline().split())
    apples.append([row-1, col-1])

L = int(sys.stdin.readline())
movement = []
for i in range(L):
    X, C = sys.stdin.readline().split()
    movement.append([int(X), C])
movement.append([0, 0])

# 1북, 2동, 3남, 4서
direction = 2
now_time = 0

move_index = 0
head_row = 0
head_col = 0
body = [[0, 0]]
while True:
    now_time += 1
    # 한 칸 이동
    if direction == 1:
        head_row -= 1
    elif direction == 2:
        head_col += 1
    elif direction == 3:
        head_row += 1
    else:
        head_col -= 1
    # 이동칸이 벽인경우
    if head_row < 0 or head_row >= N or head_col < 0 or head_col >= N:
        break
    # 이동칸이 몸인 경우
    if [head_row, head_col] in body:
        break
    # 이동칸이 사과인 경우
    if [head_row, head_col] in apples:
        apples.remove([head_row, head_col])
        body.insert(0, [head_row, head_col])
    # 이동칸이 아무 것도 아닌 경우
    else:
        body.insert(0, [head_row, head_col])
        body.pop()

    if movement[move_index][0] == now_time:
        if movement[move_index][1] == 'L':
            direction -= 1
            if direction < 1:
                direction = 4
        else:
            direction += 1
            if direction > 4:
                direction = 1
        move_index += 1

print(now_time)
