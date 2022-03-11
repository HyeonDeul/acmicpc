N, M = map(int, input().split())
pack, indiv = float('inf'), float('inf')

for _ in range(M):
    p, i = map(int, input().split())
    pack = p if p < pack else pack
    indiv = i if i < indiv else indiv

if pack > indiv*6:
    price = indiv*N
else:
    if indiv*(N % 6) >= pack:
        price = pack*(N//6+1)
    else:
        price = pack*(N//6) + indiv*(N % 6)

print(price)
