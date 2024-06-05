// 2. C program to print table of a number and power of a number (with arg no return)
#include<stdio.h>
#include<stdlib.h>
void table(int n)
{
    int i;
    for(i=1;i<=10;i++)
    {
        printf("%d * %d = %d\n",n,i,n*i);
    }
}
void power(int n,int Exponent)
{
    int i,res=1;
    for(i=1;i<=Exponent;i++)
    {
        res=res*n;
    }
    printf("%d ^ %d = %d\n",n,Exponent,res);
}
int main()
{
    int n,Exponent;
    system("cls");
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Table of %d:\n",n);
    table(n);
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Exponent:");
    scanf("%d",&Exponent);
    power(n,Exponent);
    return 0;
}