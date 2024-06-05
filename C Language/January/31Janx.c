#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() 
{
    char str1[100], str2[100];
    int i, j, palindrome = 0;
    system("cls");

    printf("Enter the first string: ");
    gets(str1);
    printf("Enter the second string: ");
    gets(str2);

    if (strlen(str1) != strlen(str2)) {
        printf("The strings are not equal.\n");
        return 0;
    } else {
        printf("The strings are equal.\n");
    }

    for (i = 0, j = strlen(str1) - 1; i < j; i++, j--) {
        if (str1[i] != str2[j]) {
            palindrome = 1;
            break;
        }
    }
    if (palindrome == 0) {
        printf("The strings are palindrome.\n");
    } else {
        printf("The strings are not palindrome.\n");
    }
    return 0;
}

