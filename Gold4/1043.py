from collections import deque

N, M = map(int, input().split())

truth = list(map(int, input().split()))
truthPeople = truth[1:]

meets = {}
parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    for i in range(party[0]):
        idx = i+1
        now = party[idx]
        if now not in meets:
            meets[now] = party[1:idx]+party[idx+1:]
        else:
            meets[now].extend(party[1:idx]+party[idx+1:])
    parties.append(party)

answer = 0

for i in meets:
    meets[i] = set(meets[i])

queue = deque(truthPeople)
while queue:
    truthPerson = queue.pop()
    if truthPerson in meets:
        gap = list(meets[truthPerson]-set(truthPeople))
        truthPeople.extend(gap)
        queue.extend(gap)

for party in parties:
    if len(set(truthPeople) & set(party[1:])) == 0:
        answer += 1
print(answer)
