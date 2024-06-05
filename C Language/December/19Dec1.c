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
            
            switch(pwd)
                {
                    case 1234:
                    printf("Welcome user 1");
                    break;
                    
                    default:
                    printf("Invalid password");
                }
            break;
            default:
            printf("Invalid user id");
        }
    printf("\n\n");
    system("pause");
    return 0;
}
