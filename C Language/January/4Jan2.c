//Print the factorial of a number (using for loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,n,f=1;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        f=f*i;
    }
    printf("\nFactorial of %d is %d\n\n",n,f);
    system("pause");
    return 0;
}