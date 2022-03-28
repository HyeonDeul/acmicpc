n = int(input())
i = 1
while n > 2**i:
    i += 1
print((n-2**(i-1))*2 if n != 1 else 1)
