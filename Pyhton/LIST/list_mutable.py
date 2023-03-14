''' List is a mutable object that means 
we can alter or replace the existing list object'''

lst = [10,20,30,'python',True,1.5,2+3j]
print(lst)   # [10, 20, 30, 'python', True, 1.5, (2+3j)]


lst[0] = 100
print(lst)    # [100, 10, 20, 30, 'python', True, 1.5, (2+3j)]

del lst[2]
print(lst)  # [100, 20, 'python', True, 1.5, (2+3j)]


'''List concatination'''
l1 = [1,3,3,4,5,10]
l2 = [10,50,70,80]
l3 = [43,22,13]
print(l1+l2)    # [1, 3, 3, 4, 5, 10, 10, 50, 70, 80]
print(l2+l1+l3) # [10, 50, 70, 80, 1, 3, 3, 4, 5, 10, 43, 22, 13]

"""List Multiplication"""
print(l1*3)  # [1, 3, 3, 4, 5, 10, 1, 3, 3, 4, 5, 10, 1, 3, 3, 4, 5, 10]
print(l2*2)  # [10, 50, 70, 80, 10, 50, 70, 80]
print(l3*5)  # [43, 22, 13, 43, 22, 13, 43, 22, 13, 43, 22, 13, 43, 22, 13]