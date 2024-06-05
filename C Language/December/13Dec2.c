#include<stdio.h>
#include<stdlib.h>
int main()
{
    char c;
    system("cls");
    printf("Enter a alphabet:");
    scanf("%c",&c);
    if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')

    {
        printf("The alphabet is vowel\n\n");
    }
    else
    {
        printf("The alphabet is consonant\n\n");
    }
    system("pause");
    return 0;
}