#include<stdio.h>
#include<stdlib.h>
int main()
{
    int year;
    system("cls");
    printf("Enter the year: ");
    scanf("%d",&year);
    (year%4==0) ? (year%100!=0? printf("The year %d is a leap year\n\n",year)
     : (year%400==0 ? printf("The year %d is a leap year\n\n",year) 
         : printf("The year %d is not a leap year\n\n",year))) 
             : printf("The year %d is not a leap year\n\n",year); 
    system("pause");
    return 0;
}