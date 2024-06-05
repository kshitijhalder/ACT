// C program to print 1-5 minus 1 in each line
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j,sum=5;
    system("cls");
    for(i=5;i>=1;i--)
    {
        for(j=1;j<=i;j++)
        {
            printf("%d\t",j);
            sum++;
        }
        printf("\n");
    }
    return 0;
}