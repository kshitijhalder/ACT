// C program to print hollow rectangle or square star pattern
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");

    for(i=1;i<=5;i++)
    {
        for(j=1;j<=5;j++)
        {
            if(i==1||i==5||j==1||j==5)
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
    return 0;
}