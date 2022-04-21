import sys
from collections import deque

V = int(sys.stdin.readline())
tree = {}

for _ in range(V):
    line = list(map(int, sys.stdin.readline().split()))
    now = line[0]
    tree[now] = []
    for i in range(len(line)//2-1):
        tree[now].append([line[2*i+1], line[2*i+2]])


def DFS(n):
    visit = [-1]*(V+1)
    que = deque([n])
    visit[n] = 0
    long_node, long_dis = 0, 0

    while que:
        now = que.pop()
        for next, dis in tree[now]:
            if visit[next] == -1:
                visit[next] = visit[now]+dis
                que.append(next)
                if long_dis < visit[next]:
                    long_node = next
                    long_dis = visit[next]

    return long_node, long_dis


node, dis = DFS(1)
node, dis = DFS(node)
print(dis)
