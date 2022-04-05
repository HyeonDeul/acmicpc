while True:
    line = input()
    if line == '.':
        break

    arr = []
    can = True

    for l in line:
        if l == '(':
            arr.append(l)
        elif l == ')':
            if len(arr) == 0:
                can = False
            else:
                if arr.pop() != '(':
                    can = False
        elif l == '[':
            arr.append(l)
        elif l == ']':
            if len(arr) == 0:
                can = False
            else:
                if arr.pop() != '[':
                    can = False

    print('yes' if can and len(arr) == 0 else 'no')
