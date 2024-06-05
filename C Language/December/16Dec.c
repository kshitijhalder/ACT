#include<stdio.h>
#include<stdlib.h>
int main()
{   
    char a;
    system("cls");
    printf("Enter a character: ");
    scanf("%c",&a);
    printf("ASCII value of %c = %d",a,a);

    if (a>=65 && a<=90)
    {
        printf("\n%c is a capital letter",a);
    }
    else if (a>=97 && a<=122)
    {
        printf("\n%c is a small letter",a);
    }
    else if (a>=48 && a<=57)
    {
        printf("\n%c is a digit",a);
    }
    else if ((a>=0 && a<=47)||(a>=58 && a<=64)||
            (a>=91 && a<=96)||(a>=123 && a<=127))
    {
        printf("\n%c is a special character",a);
    }
    printf("\n\n");
    system("pause");
    return 0;
}