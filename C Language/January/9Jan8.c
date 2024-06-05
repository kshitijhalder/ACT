// C program to print upper and lower case alphabets in triangle shape (top to bottom)
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
            printf("%c%c\t",sum+64,sum+96);
            sum++;
        }
        printf("\n");
    }
    return 0;
}