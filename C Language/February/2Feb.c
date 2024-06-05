// C program to find the sum of first n natural numbers (with arg with return)
#include <stdio.h>
#include <stdlib.h>
int total(int num)
{
    int sum = 0;
    for (int i = 1; i <= num; i++)
    {
        sum += i;
    }
    return sum;
}

int main()
{
    int num;
    system("cls");
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("The sum of first %d natural numbers is %d", num, total(num));
    return 0;
}