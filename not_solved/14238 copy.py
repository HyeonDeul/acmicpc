from collections import deque

graph = {'A': 0, 'B': 0, 'C': 0}

works = list(map(str, input()))
days = len(works)

for w in works:
    graph[w] += 1
cba = float('inf')
for i in graph:
    cba = min(cba, graph[i])

answer = 'CBA'*cba
canMake = False

zero = []
notzero = []
for i in graph:
    graph[i] -= cba
    if graph[i] == 0:
        zero.append(i)
    else:
        notzero.append(i)

if len(zero) == 1:
    if 'A' in zero:
        if graph['B'] < 3 and graph['C'] < 2:
            canMake = True
            answer += 'BC'
            if graph['B'] == 2:
                answer += 'B'

    elif 'B' in zero:
        if graph['A'] >= (graph['C']-1)*2:
            canMake = True
            answer += 'CAA'*graph['C']
            gap = graph['A']-(graph['C']*2)
            if gap > 0:
                answer += 'A' * gap
            elif gap < 0:
                answer = answer[:gap]
    else:
        if graph['B'] <= graph['A']+1:
            canMake = True
            l = min(graph['A'], graph['B'])
            answer += 'BA'*l
            if graph['B']-l > 0:
                answer += 'B'
            else:
                answer += 'A'*(graph['A']-l)
elif len(zero) == 2:
    i = notzero[0]
    if i == 'A':
        canMake = True
        answer += 'A' * graph[i]
    elif graph[i] == 1:
        canMake = True
        answer += i
else:
    canMake = True

print(answer if canMake else -1)
