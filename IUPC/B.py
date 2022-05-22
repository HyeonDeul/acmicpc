total = 0
grade = 0

score = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3,
         'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0}

for _ in range(20):
    a, b, c = map(str, input().split())
    if c != 'P':
        total += int(b[0])
        grade += int(b[0]) * score[c]

print(grade/total)
