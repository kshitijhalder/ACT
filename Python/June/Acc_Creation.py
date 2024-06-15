"""
Enter user name : [ Only alphabets, no special characters, no numbers, no spaces]
Enter password : [ Minimum 8 characters, atleast 1 upper and 1 lowercase alphabet, atlease 1 
                   special character, number]

Date : 11-04-2024
"""
import re, os

os.system('clear')

def check_username(username):
    # Username should contain only alphabets
    if re.match('^[a-zA-Z]+$', username):
        return True
    else:
        return False

def check_password(password):
    RE_pwd = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password)
    # Password should contain atleast 1 uppercase, 1 lowercase, 1 digit, 1 special char and min 8 char
    if RE_pwd:
        return True
    else:
        # Identify the error in the password
        if len(password) < 8:
            print("Password should contain minimum 8 characters")
        elif not re.search("[a-z]", password):
            print("Password should contain atleast 1 lowercase alphabet")
        elif not re.search("[A-Z]", password):
            print("Password should contain atleast 1 uppercase alphabet")
        elif not re.search("[0-9]", password):
            print("Password should contain atleast 1 digit")
        elif not re.search("[.@$!%*?&]", password):
            print("Password should contain atleast 1 special character")
        return False

def login(username, password):
    while True:
        os.system('clear')
        UID = input("\n\n\t\t\t\t\tUser name: ")
        PWD = input("\t\t\t\t\tPassword:  ")
        if UID == username and PWD == password:
            print("\n\n\n\t\t\t\t\tLogin successful")
            return True
        else:
            print("\n\n\n\t\t\t\tUsername or password is incorrect")
            return False
        
print("\n\n\t\t\t\t|Create Account - 1| \n\t\t\t\t|Sign in\t- 2| \n\n")
username = None
password = None
while True:
    input_1 = int(input("Enter your choice: "))
    if input_1 == 1:
        while True:
            os.system('clear')
            username = input("\n\n\t\t\t\t\tEnter user name: ")
            password = input("\t\t\t\t\tEnter password: ")

            id = check_username(username)
            passw = check_password(password)

            if id is False:
                print("Username should contain only alphabets")
                continue

            if passw is False:
                print("Password should contain 1 uppercase, 1 special character, number and minimum 8 characters")
                continue

            break

        login_choice = input("\n\n\tAccount created. Do you want to log in now? (yes/no): ")
        if login_choice.lower() == 'yes':
            login(username, password)

    elif input_1 == 2:
        login(username, password)
    else:
        print("\n\nInvalid choice")
    break