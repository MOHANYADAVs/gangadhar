'''Create a dictionary from list of strings 
where the first char of the string will act as key and respecctive strings are stored as values.'''
user_str = input("Enter string: ")  # apple orange animal cricket ball ballon
words = user_str.split()
d = {}
for str in words:
    ch = str[0]
    if ch not in d:
        d[ch] = []
    d[ch].append(str)
print(d)   # 'a': ['apple', 'animal'], 'o': ['orange'], 'c': ['cricket'], 'b': ['ball', 'ballon']}


# for k,v in d.items():
    # print(k,":",v)