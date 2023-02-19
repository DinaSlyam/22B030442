def perfectSquares(l, r):


    for i in range(l, r + 1):


        if (i**(.5) == int(i**(.5))):

            print(i, end=" ")


l = int(input("Enter the start of range: "))
r= int(input("Enter the end of range: "))


perfectSquares(l, r)
