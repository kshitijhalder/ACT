//Program to check whether a number is Armstrong or not (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    int r,sum=0,i;
    i=n;
    while(n>0)
    {
        r=n%10;
        sum=sum+(r*r*r);
        n=n/10;
    }
    if(i==sum)
    {
        printf("Armstrong number");
    }
    else
    {
        printf("Not an Armstrong number");
    }
    printf("\n");
    system("pause");
    return 0;
}