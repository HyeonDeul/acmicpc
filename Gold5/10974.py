def func(arr, ans=''):
    l = len(arr)
    if l == 1:
        ans += str(arr.pop())
        print(ans)
    else:

        for i in range(l):
            temparr = arr[:]
            tempans = ans+str(temparr.pop(i))+' '
            func(temparr, tempans)


n = int(input())

arr = [i for i in range(1, n+1)]


func(arr)
