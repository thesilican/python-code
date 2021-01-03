#include <stdio.h>

int findComplement(int num) {
    int cpy = num,
        mask = 0;
    while (cpy != 0) {
        cpy >>= 1;
        mask = (mask << 1) + 1;
    }
    return ~num & mask;
}

int main(int argc, char const *argv[]) {
    for (int i = 0; i < 100; i++) {
        printf("%d %d\n", i, findComplement(i));
    }
    return 0;
}
