# 마름모 : 활성화 대문자, 아니면 소문자
# 별 : 마지막으로 입력한 알파벳의 대소문자

inputstr = input()

# 1개는 별
# 여러개는 마름모
# 중간에 1개는 별
stack = []
up = False
temp = ''
for i in inputstr:
    if up:
        # 대문자인 경우
        if 65 <= ord(i) <= 90:
            temp += i
        else:
            stack.append(temp)
            temp = i
            up = False
    else:
        # 대문자인 경우
        if 65 <= ord(i) <= 90:
            stack.append(temp)
            temp = i
            up = True
        else:
            temp += i
stack.append(temp)

if stack[0] == '':
    del stack[0]

up = False

cnt = 0
for i in stack:
    cnt += len(i)
    # 대문자인데 안 캡슬락
    if 65 <= ord(i[0]) <= 90 and not up:
        if len(i) != 1:
            up = not up
        cnt += 1
    # 소문자인데 캡슬락
    elif 97 <= ord(i[0]) <= 122 and up:
        if len(i) != 1:
            up = not up
        cnt += 1

print(cnt)
