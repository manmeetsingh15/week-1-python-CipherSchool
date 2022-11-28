def msquare(n):
    square=[[0 for x in range(n)]
                   for y in range(n)]
    i=n//2
    j=n-1
    num=1
    while num <= (n*n):
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if square[int(i)][int(j)]:
            j=j-2
            i=i+1
            continue
        else:
            square[int(i)][int(j)]=num
            num=num+1
        j=j+1
        i=i-1 
    print("Sum of each row or column:",n*(n*n+1)//2)
 
    for i in range(0,n):
        for j in range(0,n):
            print('%2d '% (square[i][j]),
                  end='')
            if j==n-1:
                print()
def introduction():
    print()
    print("    𝓦𝓔𝓛𝓒𝓞𝓜𝓔!! ")
    print()
    n=int(input("Enter an odd number for dimension:"))
    if n%2!=0:
        msquare(n)
    else:
        print()
        print()
        print("Enter an ODD number!!!!")
        a=input("Enter y to continue:")
        if a=="y" or a=="Y":
            introduction()
introduction()