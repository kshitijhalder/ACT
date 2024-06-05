// C program to print 5 to 1 in 5 rows and 5 columns (right to left)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");
    for(i=5;i>=1;i--)
    {
        for(j=5;j>=1;j--)
        {
            printf("%d\t",j);
        }
        printf("\n");
    }
    system("pause");
    return 0;
            
}