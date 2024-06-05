//Program to print the Fibonacci series (using do while loop)
//Needs to be modified
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n=6,i=-3,j=3,sum=0;
    system("cls");

    do
    {
        sum=i+j;
        i=j;
        j=sum;
        printf("\t%d",sum);
        n--;
          
        
    } while (n>0);
    
    printf("\n");
    system("pause"); 
}