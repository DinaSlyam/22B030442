def main():
    file = open( "row.txt", "r" )
    lines = file.readlines()
    file.close()

    countStoimost = 0

    for line in lines:
        line = line.strip()
        print( line )

        if line.find ( "Стоимость")! = -1:
            countStoimost = countStoimost + 1

    print ("countStoimost: ", countStoimost )

main( )
