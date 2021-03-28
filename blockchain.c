#include "hash.h"
#include <string.h>



typedef unsigned char BYTE;
//initialize function
struct Blockchain* initialize(){
    //create an empty blockchain
    struct Blockchain* chain = (struct Blockchain*)malloc(sizeof(struct Blockchain));
    chain->head = NULL;
    chain->size = 0;
    return chain;
}

//add function
void add(struct Blockchain *chain, int data){
    struct Block *newBlock = (struct Block *)malloc(BLOCK_SIZE);
    newBlock->data = data;
    newBlock->prevBlock = chain->head;
    chain->head = newBlock;
    struct Block *prev = newBlock->prevBlock;
    chain->size +=1;
    newBlock->height = data/10;
    if (newBlock->prevBlock != NULL) {
        newBlock->prevHash = SSHA(toString(prev), BLOCK_SIZE);
    }
}

//print function
void print(struct Blockchain *chain) {
    struct Block *head = chain->head;
    while(head != NULL) {
        printf("[%d : %d]", head->height, head->data);
        head = head->prevBlock; //segmentation fault cause
    }
    printf("\n");
}


int verify(struct Blockchain *chain) {
    struct Block *head = chain->head;
    struct Block *prev = head->prevBlock;
    unsigned char *digestPrev;
    while (head->prevBlock != NULL) {
        digestPrev = SSHA(toString(head->prevBlock), BLOCK_SIZE);
        for (int i=0; i<DIGEST_SIZE; i++) {
            if (digestPrev[i] != head->prevHash[i]) {
                printf("Verification failed: block %d\n", prev->height);
                return 1;
            }
        }
        head = head->prevBlock;
    }
    printf("All verified\n");
    return 0;
}

int main(){
    struct Blockchain *blockchain = initialize();
    for (int i = 1; i<=20; i++){
        add(blockchain, 10*i);
    }
    print(blockchain);
    verify(blockchain);

    verify(blockchain);
    print(blockchain);
    return 0;
}
