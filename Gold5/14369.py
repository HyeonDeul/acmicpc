n = int(input())

for case in range(1, n+1):
    Numbers = input()
    letterDict = {chr(i+65): 0 for i in range(26)}

    for c in Numbers:
        letterDict[c] += 1

    nums = [0]*10

    if letterDict['Z']:
        z = letterDict['Z']
        nums[0] += z
        letterDict['Z'] -= z
        letterDict['E'] -= z
        letterDict['R'] -= z
        letterDict['O'] -= z

    if letterDict['X']:
        x = letterDict['X']
        nums[6] += x
        letterDict['S'] -= x
        letterDict['I'] -= x
        letterDict['X'] -= x

    if letterDict['S']:
        s = letterDict['S']
        nums[7] += s
        letterDict['S'] -= s
        letterDict['E'] -= s*2
        letterDict['V'] -= s
        letterDict['N'] -= s

    if letterDict['W']:
        w = letterDict['W']
        nums[2] += w
        letterDict['T'] -= w
        letterDict['W'] -= w
        letterDict['O'] -= w

    if letterDict['G']:
        g = letterDict['G']
        nums[8] += g
        letterDict['E'] -= g
        letterDict['I'] -= g
        letterDict['G'] -= g
        letterDict['H'] -= g
        letterDict['T'] -= g

    if letterDict['T']:
        t = letterDict['T']
        nums[3] += t
        letterDict['T'] -= t
        letterDict['H'] -= t
        letterDict['R'] -= t
        letterDict['E'] -= t*2

    if letterDict['U']:
        u = letterDict['U']
        nums[4] += u
        letterDict['F'] -= u
        letterDict['O'] -= u
        letterDict['U'] -= u
        letterDict['R'] -= u

    if letterDict['O']:
        o = letterDict['O']
        nums[1] += o
        letterDict['O'] -= o
        letterDict['N'] -= o
        letterDict['E'] -= o

    if letterDict['F']:
        f = letterDict['F']
        nums[5] += f
        letterDict['F'] -= f
        letterDict['I'] -= f
        letterDict['V'] -= f
        letterDict['E'] -= f

    if letterDict['N']:
        n = letterDict['N']//2
        nums[9] += n
        letterDict['N'] -= n*2
        letterDict['I'] -= n
        letterDict['E'] -= n

    answer = ''

    for i in range(10):
        answer += chr(i+48)*nums[i]

    print(f'Case #{case}: {answer}')
