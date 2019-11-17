n = int(input("enter the number of row"))
for i in range(1,n+1):
    col=int('*' * i)**2 # here one is multiplyed by i
    print(col)
