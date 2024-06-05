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
        printf("%c",ch[i]);
        if(ch[i]==' ')
        {
            printf("\n");
        }
    }
    return 0;
}