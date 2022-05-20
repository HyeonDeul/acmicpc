inputStr = input()
explode = input()

stack = []
last = explode[-1]
l = len(explode)

for i in inputStr:
    stack.append(i)
    if i == last and ''.join(stack[-l:]) == explode:
        # save = save[:-l]
        del stack[-l:]
answer = ''.join(stack)

print(answer if len(answer) > 0 else 'FRULA')
