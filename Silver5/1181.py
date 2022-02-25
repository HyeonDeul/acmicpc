import sys

while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break

    pel = True
    l = len(N)//2
    for i in range(l):
        if N[i] != N[-1*i-1]:
            pel = False
            break
    print('yes' if pel else 'no')
