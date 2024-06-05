#include<stdio.h>
#include<stdlib.h>
int main()
{
    char a,b;
    system("cls");
    printf("Enter the character: ");
    scanf("%c",&a);
    printf("Ascii value of %c is %d",a,a);

    if (a>=65 && a<=90)
    {
        b=a+32;
        printf("\nLower case of %c is %c",a,b);
    }
    else if (a>=97 && a<=122)
    {
        b=a-32;
        printf("\nUpper case of %c is %c",a,b);
    }
    else
    {
        printf("\n%c is not an alphabet",a);
    }
    printf("\n\n");
    system("pause");
    return 0;
}