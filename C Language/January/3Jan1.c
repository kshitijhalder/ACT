//Print all even numbers between 1 to 20 using for loop 
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i;
    system("cls");
    for(i=2;i<=20;i+=2)
    {
        printf("%d\n",i);
    }
    system("pause");
    return 0;
}