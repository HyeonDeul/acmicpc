import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input.split())

roads = []
for _ in range(M):
    roads.append(list(map(int, input.split())))

temp = [1 for _ in range(N-2)]
for _ in range(N-2):
    temp.append(2)

nodes = set(permutations(temp, N-2))
answer = float('inf')

for node in nodes:
    node = list(node)
    node_value = 0
    node.insert(0, 0)
    node.insert(1, 1)
    node.append(2)
    for road in roads:
        s, t, a, b, c = road

        if node[s] == 1 and node[t] == 1:
            node_value += a
        elif node[s] == 2 and node[t] == 2:
            node_value += c
        else:
            node_value += b
    answer = min(answer, node_value)

print(answer)


# 도로망 설계
# RGB같은 문제
