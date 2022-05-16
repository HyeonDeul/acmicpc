people = []
N = int(input())
cnt = 0
for _ in range(N):
    text = input()
    if text == 'ENTER':
        cnt += len(set(people))
        people = []
    else:
        people.append(text)
cnt += len(set(people))

print(cnt)
