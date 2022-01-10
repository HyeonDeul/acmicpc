n, k = map(int, input().split())

table = [[0]*(k+1) for _ in range(n+1)]

thing = [[0, 0]]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]   # 물건의 무게
        v = thing[i][1]   # 물건의 가치

        if j < w:   # 현재 무게가 물건 보다 작다면
            table[i][j] = table[i-1][j]  # 위의 값을 그대로
        else:
            table[i][j] = max(table[i-1][j], table[i-1][j-w]+v)
print(table[n][k])
