def solution(M, N):
    N += M//4
    M %= 4
    ans = 2*int(N**(1/2))
    M += 4*(N-(ans/2)**2)

    while M >= ans*2+1:
        M -= ans*2+1
        ans += 1

    return ans


print(solution(13, 3))
