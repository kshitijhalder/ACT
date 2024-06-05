#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    system("cls");
    printf("A-> Ahmedabad");
    printf("\nB-> Baroda");
    printf("\nS-> Surat");
    printf("\nR-> Rajkot");
    printf("\nEnter any Choice: ");
    scanf("%c",&ch);
    switch(ch)
    {
        case 'a':
        case 'A':
        printf("Std code of Ahmedabad is 079");
        break;
        case 'b':
        case 'B':
        printf("Std code of Baroda is 0265");
        break;
        case 's':
        case 'S':
        printf("Std code of Surat is 0261");
        break;
        case 'r':
        case 'R':
        printf("Std code of Rajkot is 0281");
        break;
        default:
        printf("Enter valid choice");
        break;
    }
    printf("\n\n");
    system("pause");
    return 0;
}