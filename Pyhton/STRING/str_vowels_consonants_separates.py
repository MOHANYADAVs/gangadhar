# To eparate vowels and consonants from given string
str = input("Ente Sentanc: ")
vow = "AEIOUaeiou"
vowels = ""
consonants = ""
for char in str:
    if char in vow:
        vowels+=char
    else:
        consonants+=char
print("Vowels in given string:",vowels)
print("consonants in given string:",consonants)

