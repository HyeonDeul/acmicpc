graph = {'A': 0, 'B': 0, 'C': 0}

works = list(map(str, input()))
days = len(works)

for w in works:
    graph[w] += 1

answer = ''

canWork = True

if graph['B'] > 0:
    answer += 'B'
    graph['B'] -= 1
elif graph['C'] > 0:
    answer += 'C'
    graph['C'] -= 1
else:
    answer += 'A'
    graph['A'] -= 1

if days > 1:
    if answer[0] == 'B':
        if graph['C'] > 0:
            answer += 'C'
            graph['C'] -= 1
        elif graph['A'] > 0:
            answer += 'A'
            graph['A'] -= 1
        else:
            canWork = False
    elif answer[0] == 'C':
        if graph['A'] > 0:
            answer += 'A'
            graph['A'] -= 1
        else:
            canWork = False
    else:
        answer += 'A'


for day in range(2, days):
    if not canWork:
        break

    if answer[day-2] == 'C':
        if answer[day-1] == 'B':
            if graph['A'] > 0:
                answer += 'A'
                graph['A'] -= 1
            else:
                canWork = False
        else:
            if graph['B'] > 0:
                answer += 'B'
                graph['B'] -= 1
            elif graph['A'] > 0:
                answer += 'A'
                graph['A'] -= 1
            else:
                canWork = False
    if answer[day-1] == 'B':
        if graph['C'] > 0:
            answer += 'C'
            graph['C'] -= 1
        elif graph['A'] > 0:
            answer += 'A'
            graph['A'] -= 1
        else:
            canWork = False
    else:
        if graph['B'] > 0:
            answer += 'B'
            graph['B'] -= 1
        elif graph['C'] > 0:
            answer += 'C'
            graph['C'] -= 1
        elif graph['A'] > 0:
            answer += 'A'
            graph['A'] -= 1
        else:
            canWork = False

print(answer if canWork else -1)
