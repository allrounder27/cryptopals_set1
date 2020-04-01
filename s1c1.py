str = raw_input("Enter string: ")
encoded = str.decode("hex").encode("base64")
print(encoded)
