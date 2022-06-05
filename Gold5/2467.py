N = int(input())
solutions = list(map(int, input().split()))

front = 0
back = N-1

min_value = float('inf')
min_front = 0
min_back = 0

while front != back:
    now = solutions[front]+solutions[back]
    if abs(now) < abs(min_value):
        min_value = now
        min_front = front
        min_back = back

    if now < 0:
        front += 1
    elif now > 0:
        back -= 1
    else:
        break

print(solutions[min_front], solutions[min_back])
