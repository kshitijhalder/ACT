//Program to check whether the number is palindrome or not (using while loop)
#include<stdio.h>
#include<stdlib.h>  
int main()
{
    int n,r,sum=0;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);

    int i=n;
    while(n>0)
    {
        r=n%10;
        sum=sum*10+r;
        n=n/10;
    }
    if(i==sum)
    {
        printf("The number is palindrome number");
    }
    else
    {
        printf("The number is not palindrome number");
    }
    printf("\n\n");
    system("pause");
    return 0;
}