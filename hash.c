#include "hash.h"
#include <string.h>
typedef unsigned char BYTE; //creates alias for unsigned char - byte

BYTE* SSHA(const BYTE* str, size_t size) {
    BYTE A, B, C, D, E;
    A=11;
    B=22;
    C=33;
    D=44;
    E=55;

    for (int i=0; i<size; i++) {
        for (int r = 0; r<12; r++) {
            BYTE F = (B & C) ^ D;
            BYTE oldA = A;
            A = E + F + (A>>3) + str[i] + r; //>> is a right shift by 3 bits
            E = D;
            D = C;
            C = B << 1; //left shift B by one bit
            B = oldA;

        }
    }
    BYTE *digest = (BYTE *)malloc(DIGEST_SIZE);
    digest[0] = A;
    digest[1] = B;
    digest[2] = C;
    digest[3] = D;
    digest[4] = E;
    return digest;

}


int match(unsigned char* msg1, unsigned char * msg2, int size) { //use memcpy with this
    int value = memcmp(msg1, msg2, size);
    return value;
}

void test_str() {
    char *str1 = "Hello World!";
    BYTE* digest1 = SSHA(str1, strlen(str1));
    printf("digest1 = %d, %d, %d, %d, %d\n", digest1[0],digest1[1], digest1[2], digest1[3], digest1[4]);

    char *str2 = "hello World!";
    digest1 = SSHA(str2, strlen(str2));
    printf("digest1 = %d, %d, %d, %d, %d\n", digest1[0],digest1[1], digest1[2], digest1[3], digest1[4]);
}

void test_block() {

    struct Block *block1 = (struct Block *)malloc(BLOCK_SIZE);
    block1->height = 1;
    block1->data = 25;
    block1->prevHash = NULL;
    block1->prevBlock = NULL;

    BYTE *digest1 = SSHA(toString(block1), BLOCK_SIZE);
    printf("digest1 = %d, %d, %d, %d, %d\n", 
    digest1[0],digest1[1], digest1[2], digest1[3], digest1[4]);
}

unsigned char* toString(struct Block *blk) {
    BYTE *str = (BYTE *)malloc(BLOCK_SIZE);
    memcpy(str, blk, BLOCK_SIZE);
    return str;
}
/*
int main() {
    test_block();
    match("hello", "hello", strlen("hello"));
}
*/