n = int(input())

wineList = []
maxList = [0]*n

for _ in range(n):
    wineList.append(int(input()))
maxList[0] = wineList[0]
maxList[1] = wineList[1]

for i in range(2, n):
    maxList[i] = max(maxList[i-2]+wineList[i], maxList[i-2]+wineList[i-1])

print(maxList)
