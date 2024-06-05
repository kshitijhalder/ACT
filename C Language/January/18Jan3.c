// C program to print 1-9 in a 4x5 matrix
#include <stdio.h>
#include <stdlib.h>

int main() {
    int counter = 1;

    system("cls");
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 4; ++j) {
            printf("%d ", counter);
            if (counter == 9) {
                counter = 0;
            } else {
                counter++;
            }
        }
        printf("\n");
    }

    return 0;
}