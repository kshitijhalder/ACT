// C Program to print hollow diamond star pattern
#include<stdio.h>   
#include<stdlib.h>
int main()

{
    int i,j;
    system("cls");

    for(i=1;i<=5;i++)
    {
        printf("\n");
        for(j=i;j<=5;j++)
        {
            printf("*");
        }
        for(j=1;j<=((2*i)-2);j++)
        {
            printf(" ");
        }
        for(j=i;j<=5;j++)
        {   
            printf("*");
        }
        
    }
    for(i=1;i<=5;i++)
    {
        printf("\n");
        for(j=1;j<=i;j++)
        {
            printf("*");
        }
        for(j=((2*i)-2);j<(2*5)-2;j++)
        {
            printf(" ");
        }
        for(j=1;j<=i;j++)
        {
            printf("*");
        }
    }
        
    return 0;
}