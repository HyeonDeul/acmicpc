def Leftside(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])


print(Leftside([2, 3], [3, 2], [10, 9]))
