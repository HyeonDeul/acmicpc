import sys


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    ilguanseong = True
    graph = {}

    for _ in range(N):
        number = sys.stdin.readline().rstrip()
        if ilguanseong:
            dif = False
            for i in number:
                if i not in graph:
                    pass
