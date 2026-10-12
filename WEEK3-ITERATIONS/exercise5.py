sen = input("Enter text: ")
shift = int(input("Enter the Caesar Cypher shift: "))
alp = "abcdefghijklmnopqrstuvwxyz"
encrypt = ""
decrypt = ""

for i in sen:
    if i.isalpha():
        encrypt += alp[(alp.index(i) + shift) % 26]
        decrypt += alp[(alp.index(i) - shift) % 26]

print("Encryption:", encrypt)
print("Decryption:", decrypt)
