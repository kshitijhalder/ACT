#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a;
    system("cls");
    printf("Enter a number:");
    scanf("%d",&a);
    if(a%2==0)
    {
        printf("The number is even\n\n");
    }
    else
    {
        printf("The number is odd\n\n");
    }
    system("pause");
    return 0;
}
