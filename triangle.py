def triangle(file_name,rows):
    myfile=open(file_name,'w')
    spaces=rows
    for rownum in range(rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range(rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(spaces*"  " + "".join("{:=5}".format(i) for i in PrintingList),file=myfile)
        spaces-=1
    print()

triangle("TestTest2",100)

