//Print the power of a number (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n,exp,p=1;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Enter the exponent: ");
    scanf("%d",&exp);
    while(exp!=0)
    {
        p=p*n;
        exp--;
    }
    printf("The power of the number is: %d\n\n",p);
    system("pause");
    return 0;
}