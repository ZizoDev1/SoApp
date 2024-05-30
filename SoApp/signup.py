from ncrpt import *
from getpass import getpass


fullName = ""
firstName = ""
userName = ""
lastName = ""
userEmail = ""
password = ""
rePassword = ""

print("------------Sign up------------")
print("  Please enter your information  ")


def signup():
    global fullName, firstName, lastName, userEmail, password, rePassword

    # check if user entered full name
    while True:
        fullName = input("Enter your full name \n --> ")
        if " " in fullName:
            firstName, lastName = fullName.split(" ", 1)
            break
        else:
            print("Please enter your full name with a space between first and last names.")

    userName = input("Enter your username \n --> ")
    userEmail = input("Enter your email address \n --> ")
    password = getpass("Enter your password \n --> ")
    rePassword = getpass("Re-enter your password \n -->")

# check if passwords rematch

    while password != rePassword:
        print("Passwords do not match")
        password = getpass("Enter your password \n --> ",)
        rePassword = getpass("Re-enter your password \n -->")

    print("Thank you for signing up")


signup()

fullName = encrypt(fullName)
firstName = encrypt(firstName)
lastName = encrypt(lastName)
userName = encrypt(userName)
userEmail = encrypt(userEmail)
password = encrypt(password)

