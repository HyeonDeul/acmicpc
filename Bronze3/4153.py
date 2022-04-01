while True:
    arr = list(map(int, input().split()))
    if arr.count(0) == 3:
        break
    arr.sort()
    print("right" if arr[0]**2+arr[1]**2 == arr[2]**2 else "wrong")
