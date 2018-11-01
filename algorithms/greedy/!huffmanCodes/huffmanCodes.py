def huffmanCodes(s):
    print(s)

s = "eeabacabad"

priorityMap = {}
for letter in s:
    if letter in priorityMap:
        priorityMap[letter]+=1
    else:
        priorityMap[letter]=1

print(priorityMap)
print(list(map(lambda l: (l, priorityMap[l]), priorityMap)))
print(sorted(list(priorityMap), key=lambda l: priorityMap[l], reverse=True))

