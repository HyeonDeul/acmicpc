import sys


def sent(sentences, eng, fran):
    if len(sentences) <= 1:
        list_eng = set(map(str, eng.split()))
        list_fran = set(map(str, fran.split()))
        # print(list_eng, list_fran)
        return len(list_eng & list_fran)

    else:
        sentence = sentences.split('/')[0]
        sentences = sentences[len(sentence)+1:]
        t_eng = eng
        t_fran = fran
        for word in sentence.split():
            t_eng += ' '+word
            t_fran += ' '+word

        both = min(sent(sentences, t_eng, fran),
                   sent(sentences, eng, t_fran))

        return both


for case in range(int(sys.stdin.readline())):
    sentences = ''
    n = int(sys.stdin.readline())
    eng = sys.stdin.readline().rstrip()
    fran = sys.stdin.readline().rstrip()

    for _ in range(n-2):
        sentences += sys.stdin.readline().rstrip()+'/'

    if n == 2:
        list_eng = set(map(str, eng.split()))
        list_fran = set(map(str, fran.split()))
        both = len(list_eng & list_fran)
    else:
        both = sent(sentences, eng, fran)
    print(f"Case #{case+1}: {both}")
