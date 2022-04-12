N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def paper(N, start=[0, 0]):
    blue, white = 0, 0

    if N == 1:
        if graph[start[0]][start[1]] == 1:
            return 0, 1
        else:
            return 1, 0

    else:
        color = graph[start[0]][start[1]]
        onePaper = True
        for row in range(start[0], start[0]+N):
            for col in range(start[1], start[1]+N):
                if graph[row][col] != color:
                    onePaper = False
                    break
        if onePaper:
            if color == 1:
                return 0, 1
            else:
                return 1, 0
        else:
            next = N//2
            drow = [start[0], start[0], start[0]+next, start[0]+next]
            dcol = [start[1], start[1]+next, start[1], start[1]+next]

            for i in range(4):
                x, y = paper(next, [drow[i], dcol[i]])
                white += x
                blue += y
            return white, blue


ans = paper(N)
for i in ans:
    print(i)
