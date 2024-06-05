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
    
    switch(ch)
    {
        case 'M':
            printf("\nEnter year: ");
            scanf("%f",&yr);
            month=yr*12;
            printf("\n %f year = %d month",yr,month);
            printf("\n\n");
            system("pause");
            goto l;
        case 'W':
            printf("\nEnter year: ");
            scanf("%f",&yr);
            week=yr*52;
            printf("\n %f year = %d week",yr,week);
            printf("\n\n");
            system("pause");
            goto l;
        case 'D':
            printf("\nEnter year: ");
            scanf("%f",&yr);
            day=yr*365;
            printf("\n %f year = %d day",yr,day);
            printf("\n\n");
            system("pause");
            goto l;
        case 'H':
            printf("\nEnter year: ");
            scanf("%f",&yr);
            hour=yr*8760;
            printf("\n %f year = %d hour",yr,hour);
            printf("\n\n");
            system("pause");
            goto l;
        case 'm':
            printf("\nEnter year: ");
            scanf("%f",&yr);
            minute=yr*525600;
            printf("\n %f year = %d minute",yr,minute);
            printf("\n\n");
            system("pause");
            goto l;
        case 'e':
        case 'E':
            printf("\nThank you for using this program");
            goto a;
        
        default:
            printf("\nInvalid choice");         
            
    }  
    a:
    printf("\n\n");
    return 0;
}