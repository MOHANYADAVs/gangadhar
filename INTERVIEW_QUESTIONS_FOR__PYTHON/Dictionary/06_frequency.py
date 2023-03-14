# count the frequescy(No of repeations) of word in a string show in dictionary format
str = input("Enter the sentance: ") # hi hello world hello frds
w = str.split()
d = {}
for i in w:
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i]+1
print(d)    # {'hi': 1, 'hello': 2, 'world': 1, 'frds': 1}