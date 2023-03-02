commands = list(map(int,input().split()))
commands.pop()

left = 0
right = 0
ans = 0
dis = {
    0:[0,2,2,2,2],
    1:[0,1,3,4,2],
    2:[0,3,1,3,4],
    3:[0,4,3,3,3],
    4:[0,3,4,3,3]
}

for i in commands:
    if dis[left][i] < dis[]
    
    