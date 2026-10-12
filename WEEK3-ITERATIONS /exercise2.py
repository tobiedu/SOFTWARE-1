num = int(input("Enter a number: "))
for i in range(0,num,2):
    print(i)
print("\nMULTIPLICATION TABLE:")
for i in range(1,13):
    print(f"{num} x {i} = {num*i}")
print("\nFACTORIAL VALUE:")
res = 1
for i in range(1,num + 1):
    res = res * i
print(res)
