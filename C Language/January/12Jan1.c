// C program to print hollow triangle star pattern
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");

    for(i=0;i<5;i++)
    {
        for(j=0;j<=5-i;j++)
        {
            printf(" ");
        }
        for(j=0;j<=2*i;j++)
        {
            if(j==0 || j==2*i)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    for(i=0;i<=5;i++)
    {
        printf(" *");
    }
    return 0;
}