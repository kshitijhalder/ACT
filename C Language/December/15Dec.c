#include<stdio.h>
#include<stdlib.h>
int main()
{
    char a;
    system("cls");
    printf("Enter the character: "); 
    scanf("%c",&a);

    if (a>='0' && a<='9')
    {
        printf("Number");
        
    }
    else if (a >= 'A' && a <= 'Z')
    {
        printf("Capital Alphabet");
    }
    else if (a >= 'a' && a <= 'z')
    {
        printf("Small Alphabet");
    }
    else
    {
        printf("Special Character");
    }
    printf("\n\n");
    system("pause");
    return 0;
}