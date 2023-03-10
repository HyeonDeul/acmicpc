N = int(input())

nums = [0]*(N+1)
cnt = 1

for i in range(2, N+1):
    if nums[i] == 0:
        nums[i] = 1
        multy = 2
        while (i*multy < N+1):
            nums[i*multy] = 1
            multy += 1
        cnt += 1

print(cnt)
