#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    system("cls");
    printf("Enter a alphabet: ");
    scanf("%c",&ch);
    switch(ch)
    {
        case 'a':
        case 'A':
        case 'e':
        case 'E':
        case 'i':
        case 'I':
        case 'o':
        case 'O':
        case 'u':
        case 'U':printf("Vowel");
        break;
        default:printf("Consonant");
        break;
    }
    printf("\n\n"); 
    system("pause");
    return 0;
}