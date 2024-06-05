//Program to print 1 to 5 in 5 rows and 5 columns (left to right)
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
            printf("%d\t",j);
        }
        printf("\n");
    }   
    system("pause");
    return 0;
}