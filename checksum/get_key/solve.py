QWORD_SIZE = 2**64

# unknown
checksum_size = 0x20
key = b"FlareOn2024"
checksum = [0 for _ in range(checksum_size)]

const = 0x5d1745d1745d1746
want = b"\x71\n\x05\x45\x01\x2b\x5f\x56\0\x57\r\x73\x55\x07\x45\x51\x2c\x5f\x01\x03\x51\x05\x75\r\x03\x10\x52\x7b\x5e\x50\t\x54\x55\'\x5a\x50\x13\x07\x7f\x58\x50\x54\x02\x51\x25\b\x50\x45\x52\x79\x5a\x07\x55\x0b\x07\x24\x5d\x04\x41\x5d\x7d\x5b\x56\x54"

idx = 0
while idx <= checksum_size:
    mul = (const * idx) % QWORD_SIZE
    key_idx = (idx - ((mul >> 2) * 0xb)) % QWORD_SIZE
    print(key_idx)
    checksum[idx] = want[idx] ^ key[key_idx]
    print(chr(checksum[idx]))
    idx+=1

print("".join([chr(x) for x in checksum]))
