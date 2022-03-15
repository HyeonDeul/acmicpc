import sys


def sent(sentences, eng, fran):
    if not sentences:
        return len(set(eng) & set(fran))
    else:
        sentence = sentences.pop()
        t_eng = eng[:]
        t_eng.extend(list(map(str, sentence.split())))
        t_fran = fran[:]
        t_fran.extend(list(map(str, sentence.split())))
        both = min(sent(sentences[:], t_eng, fran),
                   sent(sentences[:], eng, t_fran))
        return both


for case in range(int(sys.stdin.readline())):
    eng = []
    fran = []
    sentences = []
    n = int(sys.stdin.readline())
    eng.extend(list(map(str, sys.stdin.readline().rstrip().split())))
    fran.extend(list(map(str, sys.stdin.readline().rstrip().split())))

    for _ in range(n-2):
        sentences.append(sys.stdin.readline().rstrip())

    if n == 2:
        both = len(set(eng) & set(fran))
    else:
        both = sent(sentences, eng, fran)
    print(f"Case #{case+1}: {both}")
