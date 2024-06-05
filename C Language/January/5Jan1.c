//Print all even and odd numbers between 1 to 20 (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i=2,j=1;
    system("cls");
    printf("Even: ");
    printf("\tOdd:\n ");
    while(i<=20)
    {
        printf("%d",i);
        i+=2;
        printf("\t%d\n",j);
        j+=2;
    }
    system("pause");
    return 0;
}