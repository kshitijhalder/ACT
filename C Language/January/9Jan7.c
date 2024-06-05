// C program to print 1-15 in each line
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,sum=1;
    system("cls");
    
    for(i=1;i<=5;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("%d\t",sum++);
        }
        printf("\n");
    }
}