#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a,b;
    system("cls");
    printf("Enter the value of a:");
    scanf("%d",&a);
    printf("Enter the value of b:");
    scanf("%d",&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("The value of a and b after swapping is %d and %d\n\n",a,b);
    system("pause");
    return 0;
}
