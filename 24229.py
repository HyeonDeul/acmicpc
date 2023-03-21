N = int(input())

prev_end = 0
road = [[0, 0]]
for _ in range(N):
    start_input, end_input = map(int, input().split())
    start_idx, end_idx = -1, -1

    for i in range(len(road)):
        start, end = road[i]
        if prev_end < start_input < start:
            start_idx = i-0.5
        if start <= start_input <= end:
            start_idx = i
        if prev_end < end_input < start:
            end_idx = i-0.5
        if start <= end <= end:
            end_idx = i

        if start_idx != -1 and end_idx != -1:
            break
        prev_end = end

    if start_idx == -1 and end_idx == -1:
        road.append([start_idx, end_idx])
    if start_idx == end_idx:
        if start_idx % 1 == 0:
            continue
        else:
            road.insert(int(start_idx+0.5), [start_input, end_input])
    if end_idx == -1:
        road[i][1] = end_input
        road = road[:i+1]
    if start_idx % 1 == 0:
        if end_idx % 1 == 0:
            pass

prev = 0

while True:
    last = road.index(0, prev)-1
    jump = last - prev

    land = False

    for i in range(last+jump, last, -1):
        if road[i] == 1:
            land = True
        else:
            if land:
                prev = i+1
                break

    if not land:
        print(last)
        break
