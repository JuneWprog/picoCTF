import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_uppercase
print(ALPHABET)

enc="UFJKXQZQUNB"
key="SOLVECRYPTO"
flag1=""

for i in range(len(enc)):
    flag1+= ALPHABET[ALPHABET.index(enc[i])-ALPHABET.index(key[i])]

print (flag1)
