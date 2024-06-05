#include<stdio.h>
#include<stdlib.h>
int main()
{
    int rev,n,total=0;
    system("cls");
    printf("Enter a 4 digit number: ");
    scanf("%d",&n);
    rev=n%10;
    total=total*10+rev;
    n=n/10;
    rev=n%10;
    total=total*10+rev;
    n=n/10;
    rev=n%10;
    total=total*10+rev;
    n=n/10;
    total=total*10+n;
    printf("The reverse of the number is: %d\n\n",total);
    system("pause");
    return 0;
}