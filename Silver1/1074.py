def z(n, row, col, start=0):
    if n == 0:
        return start
    else:
        gap = 4**(n-1)
        side1 = start
        side2 = start+gap
        side3 = start+2*gap
        side4 = start+3*gap

        if row < (2**n)/2 and col < (2**n)/2:
            return z(n-1, row, col, side1)
        elif row < (2**n)/2 and col >= (2**n)/2:
            return z(n-1,  row, col-(2**n)/2, side2)
        elif row >= (2**n)/2 and col < (2**n)/2:
            return z(n-1, row-(2**n)/2, col, side3)
        else:
            return z(n-1, row-(2**n)/2, col-(2**n)/2, side4)


n, r, c = map(int, input().split())
print(z(n, r, c))
