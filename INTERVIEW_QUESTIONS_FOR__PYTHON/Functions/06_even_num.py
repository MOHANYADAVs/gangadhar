n = int(input("Enter n value: "))
def even(x):
    for i in range(0,x+1,2):
        print(i)
        # if (i%2 == 0):
            # print(i,end=",")
even(n)