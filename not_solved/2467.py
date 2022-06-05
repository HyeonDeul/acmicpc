from itertools import combinations

N = int(input())
solutions = list(map(int, input().split()))

min = float('inf')
min_com = []
for i in combinations(solutions, 2):
    if abs(sum(i)) < min:
        min = abs(sum(i))
        min_com = i

print(*min_com)
