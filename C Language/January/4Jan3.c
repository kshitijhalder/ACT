//Print the factorial of a number using while loop (ultimately same as 4Jan2.c)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i=1,n,f=1;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    while(i<=n)
    {
        f=f*i;
        i++;
    }
    printf("Factorial of %d is %d\n\n",n,f);
    system("pause");
    return 0;
}