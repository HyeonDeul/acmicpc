import sys
input = sys.stdin.readline

teams, games = map(int, input().split())
medals = []

g, s, b = map(int, input().split())
g += games

for _ in range(teams-1):
    medals.append(list(map(int, input().split())))

medals.sort(reverse=True)

ans = 1
left = games

start = -1
end = -1
for i in range(teams-1):
    if medals[i][0] > g:
        ans += 1
    elif medals[i][0] == g:
        if start == -1:
            start = i
    else:
        end = i
        break

left_b, left_s = games, games

while left_s:
    # 시작이 마지막인 경우
    if start == -1 or start == end:
        break

    if medals[start][1] == s:
        if b-medals[start][2]+1 > left_b:
            start += 1
            left_s -= 1
            ans += 1
        else:
            left_b -= b-medals[start][2]+1
            start += 1
            ans += 1
    else:
        sil = s-medals[start][1]
        # 은 차이보다도 부족한 경우
        if sil > left_s:
            break
        else:
            need_b = b-medals[start][2]+1
            # 은 같지만 동이 부족한 경우
            if need_b > games - sil or need_b > left_b:
                left_s -= sil+1
                if left_s < 0:
                    break
                start += 1
                ans += 1
            # 은 같고 브론즈로 이기는 경우
            else:
                left_s -= sil
                left_b -= need_b
                start += 1
                ans += 1

print(ans)
