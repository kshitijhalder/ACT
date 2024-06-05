#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    system("cls");
    printf("Enter a character: ");
    scanf("%c",&ch);
    if(isdigit(ch))
    {
        printf("The character is a digit");
    }
    else if(isupper(ch))
    {
        printf("The character is an uppercase letter");
    }
    else if(islower(ch))
    {
        printf("The character is a lowercase letter");
    }
    else
    {
        printf("The character is a special character");
    }
    printf("\n\n");
    system("pause");
    return 0;
}
