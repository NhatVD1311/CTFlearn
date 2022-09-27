file = open("TheMessage.txt", "r").read()
res=""
for i in file:
    if ord(i) == 32:
        res+="0"
    else:
        res+="1"
print(res)