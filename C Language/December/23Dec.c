#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int main()
{
   char ch,c;
   int q1, q2, q3, q4, q5, q6, q7, q8, q9, t, t1=0, t2=0, t3=0, t4=0, t5=0, t6=0, t7=0, t8=0, t9=0;
   system("cls");
   printf("\n\t\t\t\t\tMENU");
   printf("\n\nPizza:\t\t\t\t\t\tPrice:\t\t\tToken:");
        printf("\n\n1. Margherita\t\t\t\t\tRs. 299\t\t\tM");
        printf("\n2. Double Cheese Margherita\t\t\tRs. 399\t\t\tD");
        printf("\n3. Farm House\t\t\t\t\tRs. 399\t\t\tF");
   printf("\n\nBurger:\t\t\t\t\t\tPrice:\t\t\tToken:");
        printf("\n\n4. Veg Whopper\t\t\t\t\tRs. 199\t\t\tV");
        printf("\n5. Chicken Whopper\t\t\t\tRs. 299\t\t\tC");
        printf("\n6. Paneer King Melt\t\t\t\tRs. 299\t\t\tP");
   printf("\n\nSandwich:\t\t\t\t\tPrice:\t\t\tToken:");
        printf("\n\n7. Veggie Delight\t\t\t\tRs. 99\t\t\tG");
        printf("\n8. Chicken Teriyaki\t\t\t\tRs. 199\t\t\tT");
        printf("\n9. Paneer Tikka\t\t\t\t\tRs. 199\t\t\tK");
    printf("\n\n****************************************************************************************************");
    d:
    printf("\n\nDo you want to order something? (Y/N): ");
    fflush(stdin);
    scanf("%c", &ch);
    switch (ch)
    {
    case 'Y':
    case 'y':
    a:
        printf("\n\nChoose your token: ");
        fflush(stdin);
        scanf("%c", &ch);
        switch (ch)
        {
        case 'M':
        case 'm':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q1);
            t1=q1*299;
            printf("\n\nYou have ordered %d Margherita pizza(s).", q1);
            break;
        case 'D':
        case 'd':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q2);
            t2=q2*399;
            printf("\n\nYou have ordered %d Double Cheese Margherita pizza(s).", q2);
            break;
        case 'F':
        case 'f':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q3);
            t3=q3*399;
            printf("\n\nYou have ordered %d Farm House pizza(s).", q3);
            break;
        case 'V':
        case 'v':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q4);
            t4=q4*199;
            printf("\n\nYou have ordered %d Veg Whopper(s).", q4);
            break;
        case 'C':
        case 'c':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q5);
            t5=q5*299;
            printf("\n\nYou have ordered %d Chicken Whopper(s).", q5);
            break;
        case 'P':
        case 'p':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q6);
            t6=q6*299;
            printf("\n\nYou have ordered %d Paneer King Melt(s).", q6);
            break;
        case 'G':
        case 'g':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q7);   
            t7=q7*99;
            printf("\n\nYou have ordered %d Veggie Delight(s).", q7);
            break;
        case 'T':
        case 't':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q8);
            t8=q8*199;
            printf("\n\nYou have ordered %d Chicken Teriyaki(s).", q8);
            break;
        case 'K':
        case 'k':
            printf("\n\nEnter the quantity: ");
            scanf("%d", &q9);
            t9=q9*199;
            printf("\n\nYou have ordered %d Paneer Tikka(s).", q9);
            break;
        default:
            printf("\n\nEnter valid token!");
            goto a;
            break;
        }
        break;
    case 'N':
    case 'n':
        printf("\n\nThank you for visiting!");
        goto b;
        break;
    default:
        printf("\n\nEnter valid choice!");
        goto d;
        break;
    }
    c:
    printf("\n\nWould you like anything else? (Y/N): ");
    fflush(stdin);
    scanf("%c", &c);
    switch (c)
    {
    case 'Y':
    case 'y':
        goto a;
        break;
    case 'N':
    case 'n':
        break;
    default:
        printf("\n\nEnter valid choice!");
        goto c;
        break;
    }
    t=t1+t2+t3+t4+t5+t6+t7+t8+t9;
    printf("\n\nYour total bill is: Rs. %d",t);
    printf("\n\nThank you for ordering!");
    b:
    printf("\n\n");
    system("pause");
    return 0;
} 