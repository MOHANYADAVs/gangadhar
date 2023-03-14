# Removeing the Duplicates in the list
lst = [10,"Gangadhar",56,True,10,42,10,45,True]
unqNums = []
for items in lst:
    if items not in unqNums:
        unqNums.append(items)
print(unqNums)