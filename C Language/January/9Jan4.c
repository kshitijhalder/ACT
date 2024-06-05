// C program to print 1 to 5 in triangle shape (top to bottom)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,j;
    system("cls");

    for(i=1;i<=5;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("%d\t",j);
        } 
        printf("\n");
    }
    system("pause");
    return 0;
}