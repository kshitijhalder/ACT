// C program to print the marksheet of 5 students
#include<stdio.h>
#include<stdlib.h>

struct student
{
    int roll;
    float subject[5];
    float total;
    float average;
};
int main()
{
    struct student s[5];
    int i,j;
    system("clear");
    for(i=0;i<5;i++)
    {
        printf("Enter the roll number of student %d: ",i+1);
        scanf("%d",&s[i].roll);
        printf("Enter the marks of 5 subjects of student %d: ",i+1);
        for(j=0;j<5;j++)
        {
            scanf("%f",&s[i].subject[j]);
        }
    }
    for(i=0;i<5;i++)
    {
        s[i].total=0;
        for(j=0;j<5;j++)
        {
            s[i].total+=s[i].subject[j];
        }
        s[i].average=s[i].total/5;
    }
    system("cls");
    printf("\n------ Marksheet ------\n");
    printf("%-12s\t\t\t %-42s %-12s %-12s\n", "Roll Number", "Subject", "Total Marks", "Average");
    printf("%20s   %-12s %-12s %-12s %-12s\n", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5");
    printf("--------------------------------------------------------------------------------------------\n");
    
    for (int i = 0; i < 5; ++i) {
        printf("%-12d ", s[i].roll);
        
        for (int j = 0; j < 5; ++j) {
            printf("%-12.2f ", s[i].subject[j]);
        }

        printf("%-12.2f %-12.2f\n", s[i].total, s[i].average);
    }
    return 0;
}