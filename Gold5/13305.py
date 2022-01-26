n = int(input())

dis = list(map(int, input().split()))
cost = list(map(int, input().split()))
m = float('inf')
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    else:
        cost[i] = m

cost.pop()
cost.reverse()
dis.reverse()

oil = 0
temp_len = 0
for i in range(n-2):
    if cost[i] < cost[i+1]:
        temp_len += dis[i]
        oil += temp_len*cost[i]
        temp_len = 0
    else:
        temp_len += dis[i]

temp_len += dis.pop()
oil += temp_len*cost.pop()

print(oil)
