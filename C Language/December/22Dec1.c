#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    char ch;
    int length, width, side, radius, base, height;
    float area;
    a:
    system("cls");
    printf("\n\nEnter the first letter of the shape you want to calculate the area of: ");
    printf("\n\nR-> Rectangle");
    printf("\nS-> Square");
    printf("\nC-> Circle");
    printf("\nT-> Triangle\n\n");
    printf("Enter your choice: ");
    fflush(stdin);  
    scanf("%c", &ch);

    switch (ch)
    {
    case 'R':
    case 'r':
        printf("\nEnter the length and width of the rectangle: ");
        scanf("%d%d", &length, &width);
        area = length * width;
        printf("\nThe area of the rectangle is: %f", area);
        printf("\n\n");
        system("pause");
        goto a;
    case 'S':
    case 's':
        printf("\nEnter the side of the square: ");
        scanf("%d", &side);
        area = side * side;
        printf("\nThe area of the square is: %f", area);
        printf("\n\n");
        system("pause");
        goto a;
    case 'C':
    case 'c':
        printf("\nEnter the radius of the circle: ");
        scanf("%d", &radius);
        area = 3.14 * radius * radius;
        printf("\nThe area of the circle is: %f", area);
        printf("\n\n");
        system("pause");
        goto a;
    case 'T':
    case 't':
        printf("\nEnter the base and height of the triangle: ");
        scanf("%d%d", &base, &height);
        area = 0.5 * base * height;
        printf("\nThe area of the triangle is: %f", area);
        printf("\n\n");
        system("pause");
        goto a;
    case 'E':
    case 'e':
        printf("\n\nThank you for using the program!");
        printf("\n\n");
        system("pause");
        goto b;
    default:
        printf("\n\nInvalid choice!");
    
    }
    b:
    system("cls");
    return 0;
}