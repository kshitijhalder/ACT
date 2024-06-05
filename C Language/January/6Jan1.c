//Program to find the sum of digits of a number (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);

    int r,sum=0;
    while(n>0)
    {
        r=n%10;
        sum=sum+r;
        n=n/10;
    }
    printf("The sum of digits is: %d",sum);
    printf("\n\n");
    system("pause");
    return 0;
}