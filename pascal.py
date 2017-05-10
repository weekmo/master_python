def pascal(file_name,n):
    f=open(file_name,'w')
    row = [1]
    k = [0]
    con=n
    r=[]
    for x in range(n):
        print(((n-x)*(round(n/3/2)))*" ",' '.join("{:^{long}}".format(r,long=(n//3)) for r in row),file=f)
        #r.append(" ".join([str(i) for i in row]))
        row = [l+r for l,r in zip(row+k,k+row)]

pascal("text.txt",14)