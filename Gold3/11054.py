N = int(input())
arr = list(map(int, input().split()))

dp_orm = [1 for _ in range(N)]
dp_nrm = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_orm[i] = max(dp_orm[i], dp_orm[j]+1)
        if arr[N-i-1] > arr[N-j-1]:
            dp_nrm[N-i-1] = max(dp_nrm[N-i-1], dp_nrm[N-j-1]+1)

max_arr = 0
for i in range(N):
    arrLen = dp_orm[i]+dp_nrm[i]-1
    if max_arr < arrLen:
        max_arr = arrLen
print(max_arr)
