str = "python mca java"
l = str.split()
l1 = []
for word in l:
    # print(word[::-1],end=" ")
    l1.append(word[::-1])
print(" ".join(l1))