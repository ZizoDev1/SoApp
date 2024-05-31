# import all requird lib & function

# import ncrpt.py some function to make encrption
from ncrpt import *
# import hashing.py one function to make hashing
from hashing import *
# import sqlite3 lib to make connection between sqlite Database and python app
import sqlite3

# connect to Database File
db = sqlite3.connect("user_info.db")

# to set DataBase cursor in var
cursor = db.cursor()

# To make 2 table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS signup_info (username TEXT NOT NULL, password TEXT, email TEXT NOT NULL, firstname TEXT, lastname TEXT, PRIMARY KEY(username, email));")
cursor.execute("CREATE TABLE IF NOT EXISTS user_info (username TEXT NOT NULL, rounds INTEGER, lose rounds	INTEGER, win rounds	INTEGER, points	INTEGER, lose points INTEGER, win points INTEGER, PRIMARY KEY(username), FOREIGN KEY (username) REFERENCES signup_info (username));")
# to defline some var
fullName = ""
firstName = ""
userName = ""
lastName = ""
userEmail = ""
password = ""
rePassword = ""

print("------------Sign up------------")
print("  Please enter your information  ")

def makelistofsignup_info():
    cursor.execute("SELECT username, password, email FROM signup_info")
    alli = cursor.fetchall()
    linfo = []
    fa = ""
    for i in alli:
        r = str(i[0])
        l = str(i[1])
        fa = r + " " + l
        li = fa.split(" ")
        linfo.append(li)
    return linfo

linfo = makelistofsignup_info()

# Function to get user info to sign up with this info
def signup():
    global fullName, firstName, lastName, userEmail, password, rePassword, userName

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

    while True:
        userName = input("Enter your username \n --> ")
        username = forget(userName)
        for i in linfo:
            if username == i[0]:
                print("now, This username was used to")
            else:
                print("")
                print(i[0], username)
                print("")
                break

    while True:
        userEmail = input("Enter your email address \n --> ")
        if "@" in userEmail:
            Email = forget(userEmail)
            for t in linfo :
                if Email == i[3]:
                    print("now, email address was used to")
                else :
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

# Run Main Function sign up

signup()

# encrption all user info

# fullName = encrypt(fullName) Not important
firstName = encrypt(firstName)
lastName = encrypt(lastName)
password = encrypt(password)
# Hashing user info
try:
    # Call the hashing function and store the hashed password
    password = HashingInfo(password)
    print(f"Successfully signed up")
except Exception as e:
    print(f"An error occurred: {e}")

# to add this info to database
cursor.execute("SELECT username FROM signup_info")
cursor.execute("")
cursor.execute(f"INSERT INTO signup_info(username, password, email, firstname, lastname) VALUES(?, ?, ?, ?, ?)", (username, password, Email, firstName, lastName))

# to save all changs in database

db.commit()

db.close()
