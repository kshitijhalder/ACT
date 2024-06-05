#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    system("cls");
    int a,b,c;
    printf("A-> Additon");
    printf("\nS-> Subtraction");
    printf("\nM-> Multiplication");
    printf("\nD-> Division");
    printf("\nEnter the operation you want to perform: ");
    scanf("%c",&ch);
    printf("\nEnter the first number: ");
    scanf("%d",&a);
    printf("\nEnter the second number: ");
    scanf("%d",&b);
    switch(ch)
    {
        case 'A':
        case 'a':
            c=a+b;
            printf("\nAddition of %d and %d is %d",a,b,c);
            break;
        case 'S':
        case 's':
            c=a-b;
            printf("\nSubtraction of %d and %d is %d",a,b,c);
            break;
        case 'M':
        case 'm':
            c=a*b;
            printf("\nMultiplication of %d and %d is %d",a,b,c);
            break;
        case 'D':
        case 'd':
            c=a/b;
            printf("\nDivision of %d and %d is %d",a,b,c);
            break;
        default:
            printf("\nInvalid Input");
            break;
    }
    printf("\n\n");
    system("pause");
    return 0;
}