// C program to print diamond pattern
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
        for(k=0;k!=2*i-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }
    for(i=4;i>=1;i--)
    {
        for(j=1;j<=5-i;j++)
        {
            printf(" ");
        }
        for(k=0;k!=2*i-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }
}