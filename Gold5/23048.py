N = int(input())

nums = [0 for _ in range(N+1)]
nums[1] = 1
cnt = 1

for i in range(2, N+1):
    if nums[i] == 0:
        cnt += 1
        nums[i] = cnt
        multy = 2
        while i*multy <= N:
            nums[i*multy] = cnt
            multy += 1

print(cnt)
print(*nums[1:])
