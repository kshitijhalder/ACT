
#include <stdio.h>
#include <stdlib.h>

struct student 
{
    int rollNumber;
    float subjects[3]; 
    float totalMarks;
    float average;
};

int main() 
{
    struct student s;
    system("cls");

    for (int i = 0; i < 3; ++i) {
        printf("Enter details for Student %d:\n", i + 1);

        printf("Enter roll number: ");
        scanf("%d", &s.rollNumber);

        printf("Enter marks for 3 subjects:\n");
        for (int j = 0; j < 3; ++j) {
            printf("Enter marks for Subject %d: ", j + 1);
            scanf("%f", &s.subjects[j]);
        }

        s.totalMarks = 0;
        for (int j = 0; j < 3; ++j) {
            s.totalMarks += s.subjects[j];
        }
        s.average = s.totalMarks / 3.0;
    }
    system("cls");
    printf("\n------ Marksheet ------\n");
    for (int i = 0; i < 3; ++i) {
        printf("\nStudent %d:\n", i + 1);
        printf("Roll Number: %d\n", s.rollNumber);

        for (int j = 0; j < 3; ++j) {
            printf("Subject %d: %.2f\n", j + 1, s.subjects[j]);
        }

        printf("Total Marks: %.2f\n", s.totalMarks);
        printf("Average: %.2f\n", s.average);
    }

    return 0;
}