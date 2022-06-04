def star():
    pass


n = int(input())

line = ''
if n % 2 == 0:
    for i in range(1, 2**n):
        line = ''

else:
    for i in range(1, 2**n):
        line = ''*(2**n-2)
