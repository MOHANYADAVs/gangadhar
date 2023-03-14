n1 = int(input("Enter n1 value:"))
n2 = int(input("Enter n2 value:"))
n3 = int(input("Enter n3 value:"))
def asDes(x,y,z):
    if(x>y and x>z):
        if(y>z):
            print("Ascending: ",x,y,z)
            print("Decending: ",x,y,z)
        else:
            
    elif(y>z):
        print(y,z,x)
    else:
        print("Equal")
asDes(n1,n2,n3)