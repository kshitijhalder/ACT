// C program to print A to E in triangle shape (top to bottom)
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
            printf("%c\t",j+64);
        }
        printf("\n");
    }
    
    system("pause");
    return 0;            
}