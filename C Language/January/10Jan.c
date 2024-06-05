// C program to print * in descending order (5-1) from left to right
#include<stdio.h>
#include<stdlib.h>
int main()

{
    int i,j,sum=5;
    system("cls");

    for(i=sum;i>=1;i--)
    {
        for(j=1;j<=i;j++)
        {
            printf(" *");
        }
        printf("\n");
    }
    return 0;
}