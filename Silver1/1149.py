n = int(input())

street = []
for i in range(n):
    street.append(list(map(int, input().split())))

for i in range(1, len(street)):
    street[i][0] = min(street[i - 1][1], street[i - 1][2]) + street[i][0]
    street[i][1] = min(street[i - 1][0], street[i - 1][2]) + street[i][1]
    street[i][2] = min(street[i - 1][0], street[i - 1][1]) + street[i][2]

print(min(street[n - 1][0], street[n - 1][1], street[n - 1][2]))
