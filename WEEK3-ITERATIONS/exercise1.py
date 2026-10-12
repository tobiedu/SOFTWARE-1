num = 0
list = []
while (num >= 0):
    num = int(input("Enter a number: "))
    list.append(num)

# LIST ALL VALUES
print("All Values:")
for i in list:
    print(i)

# PRINT AVERAGE
print("\nAverage:", sum(list) / len(list))

# LIST ALL EVEN VALUES
print("\nAll Even Values:")
for i in list:
    if i % 2 == 0:
        print(i)
