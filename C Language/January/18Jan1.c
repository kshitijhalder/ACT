// C program to print alphabetical pascal triangle
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,ch,coef;
    system("cls");
    
    for(ch=1;ch<=5;ch++)
    {
        printf("\n");
        for(i=1;i<=5-ch;i++)
        {
            printf(" ");
        }
        coef=1;
        for(i=1;i<=ch;i++)
        {
            printf("%c ",coef+64);
            coef=coef*(ch-i)/i;
        }
            
    }
    return 0;
}