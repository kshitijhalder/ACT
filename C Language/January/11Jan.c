// C program to print inverted pyramid star pattern
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
        for(k=0;k!=2*(6-i)-1;k++)
        {
            printf("*");
        }   
        printf("\n");
    }
    
}