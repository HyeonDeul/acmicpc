r1, c1, r2, c2 = map(int, input().split())

m = max(abs(r1), abs(r2), abs(c1), abs(c2))

answer = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

for i in range(m):
    right_top = (2*(m-i))**2+1-2*(m-i)
    left_bottom = (2*(m-i)+1)**2-2*(m-i)

    for j in range(1, 2*(m-i)+1):
        if r1+m <= i <= r2+m and c1+m <= 2*m-i-j <= c2+m:
            answer[i-r1-m][2*m-i-j-c1-m] = str(right_top+j)
        if r1+m <= i+j-1 <= r2+m and c1+m <= 2*m-i <= c2+m:
            answer[i+j-1-r1-m][2*m-i - c1-m] = str(right_top-j+1)

    for j in range(1, 2*(m-i)+1):
        if r1+m <= 2*m-i <= r2+m and c1+m <= i+j <= c2+m:
            answer[2*m-i-r1-m][i+j-c1-m] = str(left_bottom+j)
        if r1+m <= 2*m-i-j+1 <= r2+m and c1+m <= i <= c2+m:
            answer[2*m-i-j+1-r1-m][i - c1-m] = str(left_bottom-j+1)
if r1+m <= m <= r2+m and c1+m <= m <= c2+m:
    answer[-1*r1][-1*c1] = '1'

l = max(len(answer[0][0]), len(answer[r2-r1][0]),
        len(answer[0][c2-c1]), len(answer[r2-r1][c2-c1]))

answer_str = ''

for line in answer:
    for j in range(c2-c1+1):
        if j == c2-c1:
            answer_str += ' '*(l-len(line[j]))+line[j]+'\n'
        else:
            answer_str += ' '*(l-len(line[j]))+line[j]+' '

print(answer_str, end='')
