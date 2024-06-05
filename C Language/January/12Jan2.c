// C program to print A-Z triangle
#include<stdio.h>
#include<stdlib.h>
int main()
{
    char ch;
    int i,j;
    system("cls");

    for(ch='A';ch<='Z';ch++)
    {
        for(i=1;i<='Z'-ch;i++)
        {
            printf(" ");
        }
        for(j=1;j<=ch-'A'+1;j++)
        {
            printf("%c ",ch);
        }
        printf("\n");
    }
    return 0;
}