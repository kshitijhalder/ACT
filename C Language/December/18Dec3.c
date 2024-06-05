#include<stdio.h>
#include<stdlib.h>

int main()
{
    int m,yr;
    system("cls");
    printf("Enter the month number(1-12): ");
    scanf("%d",&m);
    printf("Enter the year: ");
    scanf("%d",&yr);
    switch (m)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            printf("Number of days is 31");
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            printf("Number of days is 30");
            break;
        case 2:
            printf("Number of days is %d",((yr%4==0 && yr%100!=0) || yr%400==0)?29:28);
            break;
        default:
            printf("Invalid input");
            break;
    }
    printf("\n\n");
    system("pause");
    return 0;
}