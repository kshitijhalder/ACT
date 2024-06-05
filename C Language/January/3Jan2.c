//Print the sum of first n natural numbers using for loop
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,n,sum=0;
    system("cls");
    printf("Enter the number of terms: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        sum+=i;
    }
    printf("The sum of first %d natural numbers is %d\n",n,sum);
    system("pause");
    return 0;
}