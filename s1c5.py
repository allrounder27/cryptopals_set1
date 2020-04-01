a = raw_input("Enter string 1 : ")
j = len(a)
print(j)
b = ""
while j > 0:
    b += "ICE"
    j=j-3
print(a)
print(b)
xored = ''.join(chr(ord(a[i])^ord(b[i])) for i in range(0, len(a)))
encoded = xored.encode("hex")
print(encoded)
