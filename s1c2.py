str1 = raw_input("Enter string 1 : ")
a = str1.decode("hex")
str2 = raw_input("Enter string 2 : ")
b = str2.decode("hex")
xored = ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])
print(xored)
