N, M = map(int, input().split())

chess = []
for _ in range(N):
    chess.append(list(map(str, input())))

chessW = [[0 for _ in range(M)] for _ in range(N)]
chessB = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            if chess[i][j] != 'W':
                chessW[i][j] = 1
            else:
                chessB[i][j] = 1
        else:
            if chess[i][j] != 'B':
                chessW[i][j] = 1
            else:
                chessB[i][j] = 1

min_color = float('inf')
for i in range(N-7):
    for j in range(M-7):
        min_w = 0
        min_b = 0

        for k in range(8):
            min_w += sum(chessW[i+k][j:j+8])
            min_b += sum(chessB[i+k][j:j+8])

        min_color = min(min_color, min_w, min_b)

print(min_color)
