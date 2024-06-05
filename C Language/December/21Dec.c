#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    int month,week,day,hour,minute;
    float yr;
    l:
    system("cls");
    printf("\n\nM-> Month");
    printf("\nW-> Week");
    printf("\nD-> Day");
    printf("\nH-> Hour");
    printf("\nm-> Minute");
    printf("\nEnter a choice: ");
    fflush(stdin);
    scanf("%c",&ch);
    switch (ch)
    {
        case 'M':
        case 'W':
        case 'D':
        case 'H':
        case 'm':
            break;
        default:
            printf("\nInvalid choice");
            printf("\n\n");
    }
    printf("\nEnter year: ");
    scanf("%f",&yr);
    
    switch(ch)
    {
        case 'M':
            month=yr*12;
            printf("\n %f year = %d month",yr,month);
            printf("\n\n");
            system("pause");
            goto l;
        case 'W':
            week=yr*52;
            printf("\n %f year = %d week",yr,week);
            printf("\n\n");
            system("pause");
            goto l;
        case 'D':
            day=yr*365;
            printf("\n %f year = %d day",yr,day);
            printf("\n\n");
            system("pause");
            goto l;
        case 'H':
            hour=yr*8760;
            printf("\n %f year = %d hour",yr,hour);
            printf("\n\n");
            system("pause");
            goto l;
        case 'm':
            minute=yr*525600;
            printf("\n %f year = %d minute",yr,minute);
            printf("\n\n");
            system("pause");
            goto l;        
        default:
            printf("\nInvalid choice");
                         
    } 
    system("pause");
    return 0;
}
