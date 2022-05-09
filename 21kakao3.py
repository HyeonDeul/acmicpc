from collections import deque


def solution(n, k, cmd):
    ansList = ['O']*n
    delList = deque()
    for c in cmd:
        print(k, '- [', c, '] ->', end=' ')
        if c == 'C':
            ansList[k] = 'X'
            delList.append(k)

            while k < n-1:
                if ansList[k] == 'O':
                    break
                else:
                    k += 1
            while ansList[k] == 'X':
                k -= 1
        elif c == 'Z':
            idx = delList.pop()
            ansList[idx] = 'O'
        else:
            mov = int(c[-1])
            i = 0
            while i < mov:
                if c[0] == 'U':
                    k -= 1
                else:
                    k += 1
                if ansList[k] == 'O':
                    i += 1
    return ''.join(ansList)


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
