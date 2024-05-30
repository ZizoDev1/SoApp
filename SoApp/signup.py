from ncrpt import *
from getpass import getpass
from hashing import *
import sqlite3


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
        password = getpass("Enter your password \n --> ")
        rePassword = getpass("Re-enter your password \n -->")

signup()

encrypt(fullName)
encrypt(firstName)
encrypt(lastName)
user_name = encrypt(userName)
email = encrypt(userEmail)
pass_word = encrypt(password)

try:
    # Call the hashing function and store the hashed password
    PassWord = HashingInfo(pass_word)
    Email = HashingInfo(email)
    UserName = HashingInfo(user_name)
    print(f"Successfully signed up")
except Exception as e:
    print(f"An error occurred: {e}")


