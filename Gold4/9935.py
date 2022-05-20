inputStr = input()
explode = input()

stack = []
last = explode[-1]
l = len(explode)

for i in inputStr:
    stack.append(i)
    if i == last and ''.join(stack[-l:]) == explode:
        del stack[-l:]  # 슬라이싱보다 빠름
answer = ''.join(stack)

print(answer if len(answer) > 0 else 'FRULA')
