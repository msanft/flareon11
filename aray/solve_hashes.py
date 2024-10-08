import zlib
import hashlib
import itertools

def bruteforce_crc32(target_crc32, length):
    for bytes_candidate in itertools.product(range(256), repeat=length):
        crc32_value = zlib.crc32(bytes(bytes_candidate))
        if crc32_value == target_crc32:
            return bytes_candidate
    assert False, "Not candidate found"

def bruteforce_sha256(target_sha256, length):
    for bytes_candidate in itertools.product(range(256), repeat=length):
        sha256_value = hashlib.sha256(bytes(bytes_candidate)).hexdigest()
        if sha256_value == target_sha256:
            return bytes_candidate
    assert False, "Not candidate found"

def bruteforce_md5(target_md5, length):
    for bytes_candidate in itertools.product(range(256), repeat=length):
        md5_value = hashlib.md5(bytes(bytes_candidate)).hexdigest()
        if md5_value == target_md5:
            return bytes_candidate
    assert False, "Not candidate found"

result_size = 85
result = [ord("_") for _ in range(result_size)]

result[8], result[9] = bruteforce_crc32(0x61089c5c, 2)
result[34], result[35] = bruteforce_crc32(0x5888fc1b, 2)
result[63], result[64] = bruteforce_crc32(0x66715919, 2)
result[78], result[79] = bruteforce_crc32(0x7cab8d64, 2)

result[14], result[15] = bruteforce_sha256("403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f", 2)
result[56], result[57] = bruteforce_sha256("593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6", 2)

result[0], result[1] = bruteforce_md5("89484b14b36a8d5329426a3d944d2983", 2)
result[76], result[77] = bruteforce_md5("f98ed07a4d5f50f7de1410d905f1477f", 2)
result[50], result[51] = bruteforce_md5("657dae0913ee12be6fb2a6f687aae1c7", 2)
result[32], result[33] = bruteforce_md5("738a656e8e8ec272ca17cd51e12f558b", 2)

print("".join(chr(byte) for byte in result))
