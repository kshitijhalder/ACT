//Program to print first 10 Fibonacci numbers (use do-while loop)
#include<stdio.h>   
#include<stdlib.h>
int main()

{
    int n=9,i,i1=-1,i2=1;
    system("cls");

    do
    {
        i=i1+i2;
        i1=i2;
        i2=i;
        printf("\n%d",i);
        n--;
    } while (n>0);
    printf("\n");
    system("pause");
    return 0;
}