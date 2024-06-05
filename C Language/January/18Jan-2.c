// C program to print hollow square using 1s and 0s
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
                printf("1 ");
            }
            else
            {
                printf("0 ");
            }
        }
        printf("\n");
    }
    return 0;
}