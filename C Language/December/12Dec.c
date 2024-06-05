#include<stdio.h>
#include<stdlib.h>
int main()

{
    int phy,maths,elec,eng,env,total,rollno;
    float per;
    char name;
    system("cls");
    printf("Student marksheet");
    printf("\n\n\tStudent name:");
    scanf("%s",&name);
    printf("\n\n\tStudent roll no:");
    scanf("%d",&rollno);
    printf("\n\n\tPhysics:");
    scanf("%d",&phy);
    printf("\n\n\tMaths:");
    scanf("%d",&maths);
    printf("\n\n\tElectronics:"); 
    scanf("%d",&elec);
    printf("\n\n\tEnglish:");
    scanf("%d",&eng);
    printf("\n\n\tEnvironment Science:");
    scanf("%d",&env);
    total=phy+maths+elec+eng+env;
    per=total/5;
    printf("\n\n\tTotal marks obtained:%d",total);
    printf("\n\n\tPercentage:%f",per);
    if(per>=90)
    {
        printf("\n\n\tGrade A\n\n");
    }
    else if(per>=80)
    {
        printf("\n\n\tGrade B\n\n");
    }
    else if(per>=70)
    {
        printf("\n\n\tGrade C\n\n");
    }
    else if(per>=60)
    {
        printf("\n\n\tGrade D\n\n");
    }
    else if(per>=40)
    {
        printf("\n\n\tGrade E\n\n");
    }
    else
    {
        printf("\n\n\tGrade F\n\n");
    }
    system("pause");
    return 0;
}
