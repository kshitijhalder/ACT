#include<stdio.h>
#include<stdlib.h>
int main()
{
    int year;
    system("cls");
    printf("Enter the year: ");
    scanf("%d",&year);
    (year%4==0 && year%100!=0) || (year%400==0) ? printf("Leap year\n\n") : printf("Not a leap year\n\n");
    system("pause");
    return 0;
}
