#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a,b,c,d,e,f,g,h,i,j,reverse;
    system("cls");
    printf("Enter the value:");
    scanf("%d",&a);
    b=a%10;
    c=a%100;
    d=c/10;
    e=b*10+d;
    f=a%1000;
    g=f/100;
    h=e*10+g;
    i=a/10;
    j=i/100;
    reverse=h*10+j;
    printf("The reverse of the number is %d\n\n",reverse);
    system("pause");
    return 0;
}