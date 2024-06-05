#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
    int uid, pwd;
    system("cls");
    printf("Enter your user id: ");
    scanf("%d", &uid);

    switch(uid)
    {
        case 1:
            printf("Enter your password: ");
            scanf("%d", &pwd);
            (pwd == 1234)?
            printf("Welcome user 1"):
            printf("Wrong password");
            break;
        case 2:
            printf("Enter your password: ");
            scanf("%d", &pwd);
            (pwd == 2345)?
            printf("Welcome user 2"):
            printf("Wrong password");
            break;
        case 3:
            printf("Enter your password: ");
            scanf("%d", &pwd);
            (pwd == 3456)?
            printf("Welcome user 3"):
            printf("Wrong password");
            break;
        default:
            printf("Wrong user id");
    }
    printf("\n\n");
    system("pause");
    return 0;
}