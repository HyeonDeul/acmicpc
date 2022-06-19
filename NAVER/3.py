def solution(R):
    # 0 상, 1 우, 2 하, 3 좌
    dir = 1

    graph = []

    maxRow = len(R)
    maxCol = len(R[0])

    for i in R:
        graph.append(list(map(str, i)))

    row, col = 0, 0
    cnt = 0

    if graph[0][0] == 'X':
        return cnt

    while True:
        if graph[row][col] == '.':
            graph[row][col] = [dir]
            cnt += 1
        else:
            graph[row][col].append(dir)

        dircnt = 0
        canMove = True
        while True:

            if dir == 0:
                next_row = row-1
                next_col = col
            elif dir == 1:
                next_row = row
                next_col = col+1
            elif dir == 2:
                next_row = row+1
                next_col = col
            else:
                next_row = row
                next_col = col-1

            # print(dir, next_row, next_col)
            isOpened = True

            if not 0 <= next_row < maxRow:
                isOpened = False
            elif not 0 <= next_col < maxCol:
                isOpened = False
            elif graph[next_row][next_col] == 'X':
                isOpened = False

            if isOpened:
                row = next_row
                col = next_col
                break

            dircnt += 1
            dir += 1
            if dir > 3:
                dir = 0

            if dircnt == 4:
                canMove = False
                break

        if not canMove:
            break
        if graph[next_row][next_col] == '.':
            continue

        if dir in graph[next_row][next_col]:
            break
    return cnt
