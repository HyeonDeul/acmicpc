T = input()


def solution(T):
    arr = [0, 0, 0]
    for i in T:
        if i == 'S':
            arr[0] += 1
        elif i == 'M':
            arr[1] += 1
        else:
            arr[2] += 1

    return 'S'*arr[0]+'M'*arr[1]+'L'*arr[2]


print(solution(T))
