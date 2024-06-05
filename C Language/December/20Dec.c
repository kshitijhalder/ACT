#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    int month,week,day,hour,minute;
    float yr;
    printf("M-> Month");
    printf("\nW-> Week");
    printf("\nD-> Day");
    printf("\nH-> Hour");
    printf("\nm-> Minute");
    printf("\nEnter a choice: ");
    scanf("%c",&ch);
    printf("\nEnter year: ");
    scanf("%f",&yr);
    switch(ch)
    {
        case 'M':
            month=yr*12;
            printf("\n %f year = %d month",yr,month);
            break;
        case 'W':
            week=yr*52;
            printf("\n %f year = %d week",yr,week);
            break;
        case 'D':
            day=yr*365;
            printf("\n %f year = %d day",yr,day);
            break;
        case 'H':
            hour=yr*8760;
            printf("\n %f year = %d hour",yr,hour);
            break;
        case 'm':
            minute=yr*525600;
            printf("\n %f year = %d minute",yr,minute);
            break;
        default:
            printf("\nInvalid choice");
    }
    printf("\n\n");
    system("pause");
    return 0;
}