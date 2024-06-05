#include <stdio.h>
#include <stdlib.h>
int reverse(int a)
{
    int rev,n,total=0;
    while(a>0)
    {
        rev=a%10;
        total=total*10+rev;
        a=a/10;
    }
    printf("The reverse of the number is %d\n\n",total);
}
int main()
{
    int a;
    system("cls");
    printf("Enter a number:");
    scanf("%d",&a);
    reverse(a);
    system("pause");
    return 0;
}
        