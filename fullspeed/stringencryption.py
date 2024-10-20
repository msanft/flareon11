import binascii

enc = binascii.unhexlify("1c604acfc8012f8a1c49e950fe3cd442e3c5c258c2312a1c1c58dd901a7fd0d5e3d4ebb861214eabec6b88204f0a74620de4652f60049838b42f2ee2e04c70a6dca501898041e61d585a2ecdec784652f4d7501d57223dd9db191d050c399f90")
dec = []

c = 0
for idx in range(len(enc)):
    c = (13 * c + 37) % 2**8
    dec.append(enc[idx] ^ c)

print("".join([chr(c) for c in dec]))
