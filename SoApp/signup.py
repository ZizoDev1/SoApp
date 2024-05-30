from ncrpt import *
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

    userName = input("Enter your username \n --> ").lower()

    while True:
        userEmail = input("Enter your email address \n --> ")
        if "@" in userEmail and ".com" in userEmail:
            break

        else:
            print("That's not a valid email address")
            print("----------------------")

    def ValidPass():
        while True:
            password = input(
                "Enter your password (must be at least 8 characters long and include at least one number) \n --> ")

            # Check if password meets requirements
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
            elif not any(char.isdigit() for char in password):
                print("Password must include at least one number.")
            else:
                # Ask user to re-enter password for confirmation
                rePassword = input("Re-enter your password for confirmation \n --> ")
                if password == rePassword:
                    return password
                elif password != rePassword:
                    print("Passwords do not match. Please try again.")
                    ValidPass()

    password = ValidPass()


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
    signup()


