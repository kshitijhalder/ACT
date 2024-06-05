// C program to print 5 to 1 in triangle shape (top to bottom)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");

    for (i=5;i>=1;i--)
    {
        for (j=5;j>=i;j--)
        {
            printf("%d\t",i);
        }
        printf("\n");
    }
    system("pause");
    return 0;
    
}