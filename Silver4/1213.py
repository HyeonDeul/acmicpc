arr = list(map(str, input()))
arr_set = list(set(arr))
arr_set.sort()
arr_graph = {}
neg = 0
neg_spel = ''
for i in arr_set:
    cnt = arr.count(i)
    if cnt % 2 == 1:
        neg += 1
        neg_spel = i
    arr_graph[i] = cnt//2

if neg > 1:
    print("I'm Sorry Hansoo")
else:
    pel = ''
    for i in arr_graph:
        cnt = arr_graph[i]
        if cnt != 0:
            pel += i*cnt
            arr_graph[i] = 0
    if neg == 0:
        pel += pel[::-1]
    else:
        pel += neg_spel+pel[::-1]
    print(pel)
