def algo(num):
    fail = False
    l = len(num)
    i = 0
    first = False
    last = True
    while i < l:
        if first:
            if num[i] == '0':
                pass
            elif num[i] == '1':
                first = False

        else:
            if num[i] == '0':
                if i+1 == l:
                    fail = True
                    break
                if num[i+1] == '0':
                    fail = True
                    break
                else:
                    i = i+1
                    last = True
            else:
                if last:
                    if i+1 == l:
                        fail = True
                        break
                    if num[i+1] == '1':
                        fail = True
                        break
                    else:
                        if i+2 == l:
                            fail = True
                            break
                        if num[i+2] == '0':
                            last = False
                            first = True
                        else:
                            fail = True
                            break
                else:
                    if i != 0:
                        if num[i-1] == '1':
                            if i+1 != l and num[i+1] == '0':
                                first = True
                    else:
                        fail = True
                        break
        i = i+1
    if first:
        fail = True
    if fail:
        return "NO"
    else:
        return "YES"


n = int(input())

for i in range(n):
    print(algo(input()))
