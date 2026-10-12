# PALINDROME CHECKER
sentence = input("Enter text: ")
forward = []
backward = []

# PUT SENTENCE IN FORWARD / BACKWARD LIST
for i in sentence:
    if i.isalpha():
        forward.append(i.lower())
        
for i in range(len(forward)-1,-1,-1):
    backward.append(forward[i])

# CHECK IF PALINDROME
if forward == backward:
    print("Your text IS a Palindrome!")
else:
    print("Your text is NOT a Palindrome.")