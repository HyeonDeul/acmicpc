import sys
input = sys.stdin.readline

n = int(input())

cars = []
for i in range(1, n+1):
    v, w = map(int, input().split())
    cars.append([i, v, w])

goal = {}

for i, v, w in cars:
    if v not in goal:
        goal[v] = [i, w]
    else:
        if w == goal[v][1]:
            if i > goal[v][0]:
                goal[v][0] = i
        elif w > goal[v][1]:
            goal[v] = [i, w]

answer = 0
for g in goal:
    answer += goal[g][0]
print(answer)

# Dead or Arrive
# 자동자 싸움
