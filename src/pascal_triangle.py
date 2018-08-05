def triangle(rows):

    for rownum in range (rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)
    print()

def pascal(fileName,n):
    """Prints out n rows of Pascal's triangle.
    It returns False for failure and True for success."""
    f=open(fileName,'w')
    row = [1]
    k = [0]
    counter=n-1
    for x in range(n):
        #print(row)
        #print("{}".format(" ".join(row)))
        print(((n-x)*(round(n/3/2)))*" ",' '.join("{:^{long}}".format(r,long=(n//3)) for r in row),file=f)
        #print((n-x)*" ",*row)
        #print(("{} " * len(row)).format(*row))
        row = [l+r for l,r in zip(row+k,k+row)]

pascal("text.txt",14)
pascal("text2.txt",40)
