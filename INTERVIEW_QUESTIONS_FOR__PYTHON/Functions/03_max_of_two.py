x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
z = int(input("Enter y value:"))
def maxTwo(a,b,c):
    if a>b and a>c:
        print(a,"is bigger")
    elif b>c:
        print(b,"is bigger")
    elif a == b == c:
        print("equal")
    else:
        print(c,"is bigger")
maxTwo(x,y,z)