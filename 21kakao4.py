from collections import deque
import copy


def solution(n, start, end, roads, traps):
    # graph = {i: [] for i in range(1, n+1)}
    graph = [{} for _ in range(n+1)]
    trapgraph = {i: [] for i in traps}

    for road in roads:
        x, y, z = road
        if y in graph[x]:
            if graph[x][y] > z:
                graph[x][y] = z
        else:
            graph[x][y] = z

        if x in traps:
            trapgraph[x].append(y)
        if y in traps:
            trapgraph[y].append(x)

    que = deque([[start, 0, graph]])

    ans = float('inf')

    while que:
        now, dis, now_graph = que.pop()
        if ans < dis:
            continue
        if now == end:
            if ans > dis:
                ans = dis
            break

        for next in now_graph[now]:
            next_dis = dis+now_graph[now][next]
            if next in traps:
                next_graph = copy.deepcopy(now_graph)
                for linked in trapgraph[next]:
                    # 함정에서 링크로 가는경우
                    if linked in next_graph[next]:
                        d = next_graph[next].pop(linked)
                        next_graph[linked][next] = d
                    else:
                        d = next_graph[linked].pop(next)
                        next_graph[next][linked] = d
                que.append([next, next_dis, next_graph])
            else:
                que.append([next, next_dis, now_graph[:]])

    return ans


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))
