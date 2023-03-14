def isIn(word1, word2):
    l1 = len(word1)
    l2 = len(word2)

    idx1, idx2 = 0, 0
    complete = False

    while (True):
        if word1[idx1] == word2[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1

        if idx1 == l1:
            complete = True
            break
        if idx2 == l2:
            break

    return complete


def findWord(word, wordLen, wordList, start, listLen):
    maxLen = wordLen
    maxWord = word

    for i in range(start, listLen):
        if len(wordList[i]) <= wordLen:
            continue
        elif len(wordList[i]) > wordLen+1:
            break

        if isIn(word, wordList[i]):
            newWord = findWord(wordList[i], wordLen+1, wordList, i+1, listLen)
            if maxLen < len(newWord):
                maxLen = len(newWord)
                maxWord = newWord

    return maxWord


n, word = map(str, input().split(' '))

dic = []
for _ in range(int(n)):
    newWord = input()
    if len(newWord) > 2:
        dic.append(newWord)

l = len(word)
dic.sort(key=len)

print(findWord(word, 3, dic, 0, len(dic)))
