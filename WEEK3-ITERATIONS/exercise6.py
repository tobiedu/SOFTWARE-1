nums = input("Enter a series of numbers: ")
res = nums.split()
count = 0
count2 = 0
res2 = ""
res3 = ""
for i in res:
    if int(i) % 2 == 0:
        count += 1
        res2 += str(i) + " "
        if res3.split().count(i) == 0:
            count2 += 1
            res3 += str(i) + " "

print(f"There are {count} even numbers: {res2}")
print(f"There are {count2} distinct even numbers: {res3}")