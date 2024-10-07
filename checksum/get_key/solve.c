#include <stdio.h>
#include <stdint.h>

#define CHECKSUM_SIZE 0x40
#define KEY "FlareOn2024"
#define HIGHQ(x) ((int64_t)(((__uint128_t)(x) * (__uint128_t)0x5d1745d1745d1746) >> 64))

int main() {
    uint8_t checksum[CHECKSUM_SIZE] = {0};
    const int64_t constant = 0x5d1745d1745d1746;
    const uint8_t want[CHECKSUM_SIZE] = {
        0x71, 0x0A, 0x05, 0x45, 0x01, 0x2B, 0x5F, 0x56,
        0x00, 0x57, 0x0D, 0x73, 0x55, 0x07, 0x45, 0x51,
        0x2C, 0x5F, 0x01, 0x03, 0x51, 0x05, 0x75, 0x0D,
        0x03, 0x10, 0x52, 0x7B, 0x5E, 0x50, 0x09, 0x54,
        0x55, 0x27, 0x5A, 0x50, 0x13, 0x07, 0x7F, 0x58,
        0x50, 0x54, 0x02, 0x51, 0x25, 0x08, 0x50, 0x45,
        0x52, 0x79, 0x5A, 0x07, 0x55, 0x0B, 0x07, 0x24,
        0x5D, 0x04, 0x41, 0x5D, 0x7D, 0x5B, 0x56, 0x54
    };

    for (int64_t idx = 0; idx < CHECKSUM_SIZE; idx++) {
        int64_t mul = HIGHQ(idx);
        int64_t key_idx = idx - ((mul >> 2) * 0xB);
        fprintf(stderr, "idx=%lld, mul=%lld, key_idx=%lld\n", idx, mul, key_idx);

        // Check if key_idx is within bounds
        if (key_idx < 0 || key_idx >= 11) {
            fprintf(stderr, "Index out of bounds: key_idx=%lld, idx=%lld\n", key_idx, idx);
            return 1;  // Exit with an error
        }

        checksum[idx] = want[idx] ^ KEY[key_idx];
        printf("%c", checksum[idx]);
    }

    // Print the checksum as a string
    for (int i = 0; i < CHECKSUM_SIZE; i++) {
        printf("%c", checksum[i]);
    }
    printf("\n");

    return 0;
}
