// New topic:
//User defined functions
// 1. Sum,sub,mul,div (no arg no return)

#include<stdio.h>
#include<stdlib.h>

void sum()
{
    int s,x,y;
    system("cls");
    printf("Enter two numbers:");
    scanf("%d%d",&x,&y);
    s=x+y;
    printf("Sum=%d\n",s);
}
void sub()
{
    int s,x,y;
    printf("Enter two numbers:");
    scanf("%d%d",&x,&y);
    s=x-y;
    printf("Sub=%d\n",s);
}
void mul()
{
    int s,x,y;
    printf("Enter two numbers:");
    scanf("%d%d",&x,&y);
    s=x*y;
    printf("Mul=%d\n",s);
}
void divi()
{
    int s,x,y;
    printf("Enter two numbers:");
    scanf("%d%d",&x,&y);
    s=x/y;
    printf("Div=%d\n",s);
}
int main()
{
    sum();
    sub();
    mul();
    divi();
    return 0;
}