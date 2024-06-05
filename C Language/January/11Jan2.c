// C pthread program to print an arrow pattern
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,k;
    system("cls");

    for(i=1;i<=5;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf(" ");
        }
        for(k=0;k!=i-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=5-i;j++)
        {
            printf(" ");
        }
        for(k=0;k!=(5-i)-1;k++)
        {
            printf("*");
        }
        printf("\n");
    }
}