#include<stdio.h>
#include<stdlib.h>
int main()
{
    char ch[20];
     int i;
    system("cls");
    printf("Enter a string: ");
    gets(ch);

    for(i=0;ch[i]!='\0';i++)
    {
        printf("%c\n",ch[i]);
    }
    return 0;
}