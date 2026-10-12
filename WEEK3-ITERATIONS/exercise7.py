lists = []
for i in range(4):
    seq = input("Enter a sequence of 4 digits: ")
    lists.append(seq.split())

print(lists, "\n")

for i in range(4):
    print("+-+-+-+-+")
    print(f"|{(lists[i][0],' ')[lists[i][0] == '0']}|{(lists[i][1],' ')[lists[i][1] == '0']}|{(lists[i][2],' ')[lists[i][2] == '0']}|{(lists[i][3],' ')[lists[i][3] == '0']}|")
print("+-+-+-+-+")
