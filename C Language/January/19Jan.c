//TOPIC: ARRAYS
//1d array
//C program to read and print the sum of elements in an array
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,arr[5],sum=0;
    system("cls");
    printf("Enter the elements of the array: ");

    for(i=0;i<5;i++)
    {
        scanf("%d",&arr[i]);
        sum=sum+arr[i];
    }
    printf("Sum of array elements is: %d",sum);
    return 0;
}