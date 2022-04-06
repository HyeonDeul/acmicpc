line = list(map(str, input()))
expression = ''
idx = 0
bracket = False
temp = ''
for l in line:
    if l == '+':
        expression += str(int(temp))+'+'
        temp = ''
    elif l == '-':
        expression += str(int(temp))
        temp = ''
        if bracket:
            expression += ')'
        expression += '-('
        bracket = True
    else:
        temp += l
expression += str(int(temp))
if bracket:
    expression += ')'
print(eval(expression))
