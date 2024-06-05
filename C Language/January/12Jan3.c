// C program to print pascal triangle
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,k;
    system("cls");

    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5-i;j++)
        {
            printf(" ");
        }
        k=1;
        for(j=1;j<=i;j++)
        {
            printf("%d ",k);
             k = k * (i - j) / j;
        }
        printf("\n");
    }
    return 0;
    
}