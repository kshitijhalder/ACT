//Program to print 20 to 1 using (do while loop)
#include<stdio.h>
#include<stdlib.h>
int main()

{
    int n=20;
    system("cls");
    
    do
    {
        printf("%d\n",n);
        n--;
    } while (n>=1); 
    
    system("pause");
    return 0;
}