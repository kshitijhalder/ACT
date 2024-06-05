//Print 1 to 10 and 10 to 1 (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i=1,j=10;
    system("cls");
    while(i<=10)
    {
        printf("%d\n",i);
        i++;
        printf("%d\n",j);
        j--;
    }
    system("pause");
    return 0;
}