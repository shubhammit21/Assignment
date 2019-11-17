def natural_no(n):
    sm=0
    sm1=0
    for i in range(1,n+1):
        sm=sm + (i**2)
        sm1=sm1+i

    return sm1**2 - sm
n=int(input("enter a natural number"))

print(natural_no(n))
    
