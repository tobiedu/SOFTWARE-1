num = int(input("Enter a number: "))
nums = ""
binary = ""

while num > 0:
    nums += str(num % 2)
    num = num // 2

for i in range(len(nums) - 1, -1, -1):
    binary += nums[i]

print(binary)