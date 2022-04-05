n, r, c = map(int, input().split())

graph = [[0 for _ in range(2**n)] for _ in range(2**n)]


def z(seq, now=0, row=0, col=0):
    if seq == 0:
        graph[row][col] = now
        graph[row][col+1] = now+1
        graph[row+1][col] = now+2
        graph[row+1][col+1] = now+3
        return now + 4
    else:
        now = z(seq-1, now, row, col)
        now = z(seq-1, now, row, col+2**seq)
        now = z(seq-1, now, row+2**seq, col)
        now = z(seq-1, now, row+2**seq, col+2**seq)
        return now


z(n-1)
print(graph[r][c])
