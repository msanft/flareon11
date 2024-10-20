import Crypto.PublicKey.ECC as ECC

XOR_DECRYPT_KEY = int("133713371337133713371337133713371337133713371337133713371337133713371337133713371337133713371337", 16)

client_x = int("0a6c559073da49754e9ad9846a72954745e4f2921213eccda4b1422e2fdd646fc7e28389c7c2e51a591e0147e2ebe7ae", 16) ^ XOR_DECRYPT_KEY
client_y = int("264022daf8c7676a1b2720917b82999d42cd1878d31bc57b6db17b9705c7ff2404cbbf13cbdb8c096621634045293922", 16) ^ XOR_DECRYPT_KEY

server_x = int("a0d2eba817e38b03cd063227bd32e353880818893ab02378d7db3c71c5c725c6bba0934b5d5e2d3ca6fa89ffbb374c31", 16) ^ XOR_DECRYPT_KEY
server_y = int("96a35eaf2a5e0b430021de361aa58f8015981ffd0d9824b50af23b5ccf16fa4e323483602d0754534d2e7a8aaf8174dc", 16) ^ XOR_DECRYPT_KEY

server_pubkey = ECC.EccPoint(server_x, server_y)
