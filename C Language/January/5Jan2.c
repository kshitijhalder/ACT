//Print 2,4,8,16,32,64,128,256,512,1024 (using while loop)
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i=2;
    system("cls");
    while(i<=1024)
    {
        printf("%d\n",i);
        i=i*2;
    }
    system("pause");
    return 0;
}