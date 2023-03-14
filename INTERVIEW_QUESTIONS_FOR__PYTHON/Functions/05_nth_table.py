n = int(input("Enter n value: "))
def nthTable(x):
    for i in range(1,x+1):
        print(n,"*",i,"=",n*i)
nthTable(n)