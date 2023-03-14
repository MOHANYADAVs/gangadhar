# Create a dictionary which contains numbers between 1 to n as a key and square of them as a value
n = int(input("Enter n value: "))
d = {i:i **2 for i in range(1,n+1)}
print(d)
