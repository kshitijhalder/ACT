// C program to enter number of rows and column and display the elements of the matrix
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int m,n,i,j;
    system("cls");       
    printf("Enter the number of rows and column\n");
    scanf("%d %d",&m,&n);    
    int arr[m][n];   
    printf("Enter the elements of the matrix\n");
    for(i=0;i<m;i++)     
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    printf("\nElements in the matrix are \n");
    for(i=0;i<m;i++)     
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}