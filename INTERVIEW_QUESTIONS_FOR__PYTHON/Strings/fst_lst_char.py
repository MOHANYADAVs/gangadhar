# first and last charaters remaining stars(*)
str=input("Enter any name/word: ")
print(str[0] + "*"*int(len(str)-2) + str[-1])
