#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a,b,c;
    system("cls");
    printf("Enter the value of A, B and C:");
    scanf("%d%d%d",&a,&b,&c);

    (a>b && a>c)?printf("A is greater\n\n"):(b>c)?printf("B is greater\n\n"):printf("C is greater\n\n");
    system("pause");
    return 0;
}