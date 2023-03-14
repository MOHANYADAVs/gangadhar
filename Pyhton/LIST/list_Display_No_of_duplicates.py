# Display the No of Duplicates  by using Any Number in the existing list
lst = [10,20,20,50,100,20,90,20]
num =int(input("Enter the repeated No: "))
count = 0
for items in lst:
    if items == num:
        count+=1
print( num,"is",count,'times')

