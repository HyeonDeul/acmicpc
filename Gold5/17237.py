import sys
input = sys.stdin.readline

N = int(input())
cnt = [0 for i in range(21)]

for _ in range(N):
    cnt[int(input())] += 1

for i in range(20, 0, -1):
    cnt[i-1] += cnt[i]//2
    cnt[i] %= 2

print('A' if cnt[0] > 0 else 'B')
