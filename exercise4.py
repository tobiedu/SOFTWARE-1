sen = input("Enter a sentence: ")

res = ""
for i in sen:
    if i.isalpha():
        res += i
print(res)

res = ""
cap = 1
for i in sen:
    if i.isalpha():
        if cap: 
            res += i.upper()
            cap = 0
        else:
            res += i
    else:
        cap = 1
print(res)

sen2 = input("\nEnter a sentence in CamelCase: ")
res2 = []
cur = 0
for i in range(0, len(sen2)):
    if sen2[i].isupper() and i != 0:
        res2.append(sen2[cur:i])
        cur = i
    elif i == len(sen2) - 1:
        res2.append(sen2[cur:i+1])
print(res2)