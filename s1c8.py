import binascii
string_input = open('s1c8.txt').read().splitlines()
for line in string_input:
    line_bytes = binascii.unhexlify(line)
    blocks = [line_bytes[start:start+16] for start in range(0, len(line_bytes), 16)]
    for block in blocks:
        if blocks.count(block) > 1:
            print("Detected!")
            print(line_bytes)
