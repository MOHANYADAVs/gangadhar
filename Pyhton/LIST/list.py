# Different ways of creating list
# list support Homeogenious & Hetrogenious elements


lst = [0,3,9,10,985,0]
lst1 = list([10,"Gangadhar",20,3+5j,2.5,False])
lst2 = list(range(1,10,2))
print(type(lst))  # <class 'list'>
print(type(lst1)) # <class 'list'>
print(type(lst2)) # <class 'list'>

# list support packing 
a = "python"
b = 60
c = True
lst_pack = [a,b,lst]
print(lst_pack)   # ['python', 60, [0, 3, 9, 10, 985, 0]]

# list unpack

lst_unpack = ["python",True,5,20,56]
# x,y,z = lst_unpack  # ValueError: too many values to unpack (expected 3)
# p,q,r,s,t,u,v = lst_unpack # ValueError: not enough values to unpack (expected 7, got 5)
# print(x)
# print(p)
x,y,z,p,q = lst_unpack
print(x) # python
print(y) # True
print(z) # 5
print(p) # 20
print(q) # 56 

