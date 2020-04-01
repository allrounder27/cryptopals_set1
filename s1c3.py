str1 = raw_input("Enter string : ")
a = str1.decode("hex")
print(a)
freq = {
        'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07,
        'e' : 12.0,
        't' : 9.10,
        'a' : 8.12,
        'o' : 7.68,
        'i' : 7.31,
        'n' : 6.95,
        's' : 6.28,
        'r' : 6.02,
        'h' : 5.92,
        'd' : 4.32,
        'l' : 3.98,
        'u' : 2.88,
        'c' : 2.71,
        'm' : 2.61,
        'f' : 2.30,
        'y' : 2.11,
        'w' : 2.09,
        'g' : 2.03,
        'p' : 1.82,
        'b' : 1.49,
        'v' : 1.11,
        'k' : 0.69,
        'x' : 0.17,
        'q' : 0.11,
        'j' : 0.10,
        'z' : 0.07,
    }
finalvalue = []
for x in range (256):
    j = len(a)
    b = ""
    while j > 0:
        b += chr(x)
        j=j-1
    xored = ''.join(chr(ord(a[i])^ord(b[i])) for i in range(0, len(a)))
    k = len(a)
    value = 0
    while k >= 0:
        frequency = freq.get(xored[k-1], 0)
        value = value + frequency
        k=k-1
    finalvalue.append(value)
d = 10
while d > 0:
    y = finalvalue.index(max(finalvalue))
    j = len(a)
    b = ""
    print(y)
    while j > 0:
        b += chr(y)
        j=j-1
    xored = ''.join(chr(ord(a[i])^ord(b[i])) for i in range(0, len(a)))
    print("The probable string " + str(10-d) + " is:")
    print(xored)
    finalvalue[y] = 0
    d = d-1
