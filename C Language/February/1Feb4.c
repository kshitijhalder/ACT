// C program using switch case to find reverse, palindrome or armstrong number
#include <stdio.h>
#include <stdlib.h>
int reverse(int num) 
{
    int reversed = 0;

    for (int i=0;i=num;i++)
    {
        int digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }

    return reversed;
}
int isPalindrome(int num) 
{
    return num == reverse(num);
}
int isArmstrong(int num) 
{
    int originalNum, remainder, n = 0, result = 0;

    originalNum = num;

    while (originalNum != 0) {
        originalNum /= 10;
        ++n;
    }

    originalNum = num;

    while (originalNum != 0) {
        int digit = originalNum % 10;
        int power = 1;

        int i = 0;
        while (i < n) {
            power *= digit;
            ++i;
        }

        result += power;
        originalNum /= 10;
    }

    return result == num;
}
int main() {
    int num;
    char choice;

    system("cls");
    printf("Enter a number: ");
    scanf("%d", &num);

    printf("Choose an option:\n");
    printf("R. Reverse\n");
    printf("P. Palindrome\n");
    printf("A. Armstrong\n");
    printf("Enter your choice: ");
    scanf(" %c", &choice); 

    switch (choice) {
        case 'R':
        case 'r':
            printf("Reverse of %d is: %d\n", num, reverse(num));
            break;

        case 'P':
        case 'p':
            if (isPalindrome(num)) {
                printf("%d is a palindrome.\n", num);
            } else {
                printf("%d is not a palindrome.\n", num);
            }
            break;

        case 'A':
        case 'a':
            if (isArmstrong(num)) {
                printf("%d is an Armstrong number.\n", num);
            } else {
                printf("%d is not an Armstrong number.\n", num);
            }
            break;

        default:
            printf("Invalid choice.\n");
            break;
    }

    return 0;
}