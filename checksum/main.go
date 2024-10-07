package main

import (
	"encoding/hex"
	"fmt"
	"os"

	"golang.org/x/crypto/chacha20poly1305"
)

func main() {
	// key should be randomly generated or derived from a function like Argon2.
	key, err := hex.DecodeString("7fd7dd1d0e959f74c133c13abb740b9faa61ab06bd0ecd177645e93b1e3825dd")
	if err != nil {
		panic(err)
	}

	aead, err := chacha20poly1305.NewX(key)
	if err != nil {
		panic(err)
	}

	ciphertext, err := os.ReadFile("encrypted.jpeg")
	if err != nil {
		panic(err)
	}

	nonce := make([]byte, aead.NonceSize())

	// Decrypt the message and check it wasn't tampered with.
	plaintext, err := aead.Open(nil, nonce, ciphertext, nil)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%s\n", plaintext)
}
