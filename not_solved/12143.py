import sys


def sentences():
    pass


for _ in range(int(sys.stdin.readline())):
    eng = []
    fran = []
    not_define = []

    n = int(sys.stdin.readline())
    eng.extend(list(map(str, sys.stdin.readline().rstrip().split())))
    fran.extend(list(map(str, sys.stdin.readline().rstrip().split())))

    for _ in range(n-2):
        temp = list(map(str, sys.stdin.readline().rstrip().split()))
