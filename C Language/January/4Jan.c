//Print the table of a number using for loop
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,n;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    for(i=0;i<10;i++)
    {
        printf("%d * %d = %d\n",n,i,n*i);
    }
    system("pause");
    return 0;
}