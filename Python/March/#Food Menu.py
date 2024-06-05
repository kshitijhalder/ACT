#Food Menu
#Date : 11.3.2024
import os

os.system('clear')
t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

print("\n\t\t\t\t\tMENU")
print("\nPizza:\t\t\t\t\t\tPrice:\t\t\tToken:")
print("\n1. Margherita\t\t\t\t\tRs. 299\t\t\tM")
print("2. Double Cheese Margherita\t\t\tRs. 399\t\t\tD")
print("3. Farm House\t\t\t\t\tRs. 399\t\t\tF")
print("\nBurger:\t\t\t\t\t\tPrice:\t\t\tToken:")
print("\n4. Veg Whopper\t\t\t\t\tRs. 199\t\t\tV")
print("5. Chicken Whopper\t\t\t\tRs. 299\t\t\tC")
print("6. Paneer King Melt\t\t\t\tRs. 299\t\t\tP")
print("\nSandwich:\t\t\t\t\tPrice:\t\t\tToken:")
print("\n7. Veggie Delight\t\t\t\tRs. 99\t\t\tG")
print("8. Chicken Teriyaki\t\t\t\tRs. 199\t\t\tT")
print("9. Paneer Tikka\t\t\t\t\tRs. 199\t\t\tK")
print("\n****************************************************************************************************")

D = {"M": 299, "D": 399, "F": 399, "V": 199, "C": 299, "P": 299, "G": 99, "T": 199, "K": 199}
while True:
    ch = input("\n\nDo you want to order something? (Y/N): ")
    if ch == 'y':
        token = input("\n\nChoose your token: ")

        if token == 'M' :
            quantity = int(input("\n\nEnter the quantity: "))
            t1 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Margherita pizza(s).")
        elif token == 'D':
            quantity = int(input("\n\nEnter the quantity: "))
            t2 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Double Cheese Margherita pizza(s).")
        elif token == 'F':
            quantity = int(input("\n\nEnter the quantity: "))
            t3 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Farm House pizza(s).")
        elif token == 'V':
            quantity = int(input("\n\nEnter the quantity: "))
            t4 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Veg Whopper(s).")
        elif token == 'C':
            quantity = int(input("\n\nEnter the quantity: "))
            t5 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Chicken Whopper(s).")
        elif token == 'P':
            quantity = int(input("\n\nEnter the quantity: "))
            t6 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Paneer King Melt(s).")
        elif token == 'G':
            quantity = int(input("\n\nEnter the quantity: "))
            t7 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Veggie Delight(s).")
        elif token == 'T':
            quantity = int(input("\n\nEnter the quantity: "))
            t8 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Chicken Teriyaki(s).")
        elif token == 'K':
            quantity = int(input("\n\nEnter the quantity: "))
            t9 = quantity * D[token]
            print(f"\n\nYou have ordered {quantity} Paneer Tikka(s).")
        else:
            print("\n\nEnter valid token!")
            continue
    elif ch == 'n':
        print("\n\nThank you for visiting!")
        break
    else:
        print("\n\nEnter valid choice!")
        continue

    while True:
        c = input("\n\nWould you like anything else? (Y/N): ")
        if c == 'y':
            break
        elif c == 'n':
            break
        else:
            print("\n\nEnter valid choice!")
            continue

t = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9
print("\n\nYour total bill is: Rs. ",t)
print("\n\nThank you for ordering!")



