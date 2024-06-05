#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char a;
    system("cls");
    printf("Enter a character: ");
    scanf("%c",&a);
    if(islower(a))
    {
        printf("The character is lowercase");
        printf("\nUppercase of %c is %c",a,toupper(a));
    }
    else if(isupper(a))
    {
        printf("The character is uppercase");
        printf("\nLowercase of %c is %c",a,tolower(a));
    }
    printf("\n\n");
    system("pause");
    return 0;
}