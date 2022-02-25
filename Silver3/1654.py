from re import T


k, n = map(int, input().split())
all_line = 0
lines = []
for _ in range(k):
    line = int(input())
    all_line += line
    lines.append(line)


min_line = 0
max_line = all_line//n

while True:
    line = (min_line+max_line)//2
    line_make = 0
    for i in lines:
        line_make += i//line

    if line_make > n:
        min_line = line
    elif line_make < n:
        max_line = line
    else:
        break

while True:
    line += 1
    line_make = 0
    for i in lines:
        line_make += i//line

    if line_make < n:
        print(line-1)
        break
