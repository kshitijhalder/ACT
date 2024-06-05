#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a;
    system("cls");
    printf("Enter the value of A:");
    scanf("%d",&a);

    (a%2==0)?printf("Even\n\n"):printf("Odd\n\n");
    system("pause");    
    return 0;
}