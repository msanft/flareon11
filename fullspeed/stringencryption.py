import binascii

enc = binascii.unhexlify("143540cbc0512c8f4c4db803f8698447e4c5905b90617c1f1c5d88934879d4d7b4d5e0eb60714cafec6dd8231809246704e5307b30019c3fbc7d28b3e81974f7d4f5008b8011ec4f0c0d78c3b8294407a485501b50213cdfdc1d485308399497")
dec = []

c = 0
for idx in range(len(enc)):
    c = (13 * c + 37) % 2**8
    dec.append(enc[idx] ^ c)

print("".join([chr(c) for c in dec]))
