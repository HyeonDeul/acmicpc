n = int(input())
cnt = 0
six = '666'
num = 666
while True:
    if six in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    else:
        num += 1
