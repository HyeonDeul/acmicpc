from binascii import hexlify
from collections import deque

N = int(input())

hex_angle = [1]
hex_len = 1
gap = 5

while hex_angle[hex_len-1] <= N:
    hex_angle.append(hex_angle[hex_len-1]+gap)
    hex_len += 1
    gap += 4
hex_angle.pop()
hex_len -= 1


min_hex = float('inf')
# 현재 수, 계산해야 할 idx, 카운트
queue = deque([[N, hex_len-1, 0]])

while queue:
    temp_N, idx, cnt = queue.pop()
    now = hex_angle[idx]

    if cnt > min_hex:
        continue

    if temp_N == 0:
        if cnt < min_hex:
            min_hex = cnt

    elif idx == 0:
        cnt += temp_N
        if cnt < min_hex:
            min_hex = cnt
    elif now <= temp_N:
        for i in range(temp_N//now+1):
            queue.append([temp_N-i*now, idx-1, cnt+i])
    else:
        while now > temp_N:
            idx -= 1
            now = hex_angle[idx]
        queue.append([temp_N, idx, cnt])

print(min_hex)
