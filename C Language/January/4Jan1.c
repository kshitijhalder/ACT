//Print the first and last digit of a number
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,n,f,l;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    l=n%10;
    for (i = 0; n>0; i++)
    {
        f=n%10;
        n=n/10;
    }
    printf("\nThe first digit is %d and the last digit is %d\n\n",f,l);
    system("pause");
    return 0;
}