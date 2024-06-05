// C program to print 5 to 1-5 in each line
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");

    for(i=5;i>=1;i--)
    {
        for(j=i;j<=5;j++)
        {
            printf("%d\t",j);
        }
        printf("\n");
    }

}