// C program to find factorial of given number  (no argument with return value)
#include <stdio.h>
#include <stdlib.h>
int factorial()
{
    int n, i, fact = 1;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}
int main()
{
    system("cls");
    printf("Factorial of given number is: %d", factorial());
    return 0;
}