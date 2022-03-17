import sys


def findRGB(street, RGB, prev, now, N):
    if now == N:
        print('final', RGB)
        return RGB
    else:
        print(RGB)
        temp1 = float('inf')
        temp2 = float('inf')
        if prev == 0:
            if street[now][1] <= street[now][2]:
                temp1 = findRGB(street, RGB+street[now][1], 1, now+1, N)
            if street[now][2] <= street[now][1]:
                temp2 = findRGB(street, RGB+street[now][2], 2, now+1, N)
        elif prev == 1:
            if street[now][0] <= street[now][2]:
                temp1 = findRGB(street, RGB+street[now][0], 0, now+1, N)
            if street[now][2] <= street[now][0]:
                temp2 = findRGB(street, RGB+street[now][2], 2, now+1, N)
        else:
            if street[now][1] <= street[now][0]:
                temp1 = findRGB(street, RGB+street[now][1], 1, now+1, N)
            if street[now][0] <= street[now][1]:
                temp2 = findRGB(street, RGB+street[now][0], 0, now+1, N)
        return min(temp1, temp2)


N = int(sys.stdin.readline())
street = []

for _ in range(N):
    street.append(list(map(int, sys.stdin.readline().split())))
print(street)

minRGB = float('inf')
for i in range(3):
    temp = findRGB(street, street[0][i], i, 1, N)
    if minRGB > temp:
        minRGB = temp
print(minRGB)
