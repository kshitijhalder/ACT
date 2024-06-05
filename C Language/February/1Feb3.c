// C program to find the sum of all elements (with arg with return)
#include <stdio.h>
#include <stdlib.h>
int sum(int arr[], int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
        sum += arr[i];
    return sum;
}   
int main()
{
    int size;
    system("cls");
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int arr[size];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < size; i++){
        scanf("%d", &arr[i]);
    }
    int total = sum(arr, size);
    printf("The sum of the elements of the array is %d", total);
    return 0;
}