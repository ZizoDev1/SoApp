from ncrpt import *
from getpass import getpass
from hashing import *


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
            # Check if first name true
            if fullName[0] == " ":
                print("You didn't your first name")
            else:
                firstName, lastName = fullName.split(" ", 1)
                break

        else:
            print("Please enter your full name with a space between first and last names.")

    userName = input("Enter your username \n --> ")

    while True:
        userEmail = input("Enter your email address \n --> ")
        if "@" in userEmail and ".com" in userEmail:
            print(" ")



    password = getpass("Enter your password \n --> ")
    rePassword = getpass("Re-enter your password \n -->")

# check if passwords rematch

    while password != rePassword:
        print("Passwords do not match")
        password = getpass("Enter your password \n --> ")
        rePassword = getpass("Re-enter your password \n -->")


signup()


fullName = encrypt(fullName)
firstName = encrypt(firstName)
lastName = encrypt(lastName)
userName = encrypt(userName)
userEmail = encrypt(userEmail)
password = encrypt(password)

try:
    # Call the hashing function and store the hashed password
    password = HashingInfo(password)
    Email = HashingInfo(userEmail)
    UserName = HashingInfo(userName)
    print(f"Successfully signed up")
except Exception as e:
    print(f"An error occurred: {e}")


print(password)
