// C program to print right side pyramid using *
#include<stdio.h>
#include<stdlib.h>
int main()

{
    int i,j,sum=5;
    system("cls");

    for(i=1;i<=sum;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf(" *");
        }        
        printf("\n");
    }
    return 0;
}