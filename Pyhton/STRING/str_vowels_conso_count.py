# Count The Vowels and consonants in Given String
sen = input("Enter The Sentence: ")
# sen.lower()
# lst = ["a","e","i","o","u"]
str = "AEIOUaeiou"
vow_count = 0
conso_count = 0
for char in sen:
    if char in str:
        vow_count+=1
    else:
        conso_count+=1

print("No of vowels in given sentence is:",vow_count) 
print("No of consonants in given sentence is:",conso_count) 