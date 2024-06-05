#include<stdio.h>
#include<stdlib.h>
int main()
{
    int phy,chem,maths;
    system("cls");
    printf("Enter the marks of physics, chemistry and maths respectively: ");
    scanf("%d%d%d",&phy,&chem,&maths);
    if(phy>=35)
    {
        if(chem>=35)
        {
            if(maths>=35)
            {
                printf("The student is passed\n\n");
            }
            else
            {
                printf("The student is failed\n\n");
            }
        }
        else
        {
            printf("The student is failed\n\n");
        }
    }
    else
    {
        printf("The student is failed\n\n");
    }
    system("pause");
    return 0;
}