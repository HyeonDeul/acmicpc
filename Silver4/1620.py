import sys

N, M = map(int, sys.stdin.readline().split())
monster_dict = []
for _ in range(N):
    monster_dict.append(sys.stdin.readline().rstrip())
for _ in range(M):
    t = sys.stdin.readline().rstrip()
    try:
        t = int(t)
        print(monster_dict[t-1])
    except:
        print(monster_dict.index(t)+1)
