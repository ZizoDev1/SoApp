# Import necessary libraries
from ncrpt import *
from hashing import *
import sqlite3

# Connect to the database
db = sqlite3.connect("user_info.db")
cursor = db.cursor()

# Create tables if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS signup_info (
    username TEXT NOT NULL, 
    password TEXT, 
    email TEXT NOT NULL, 
    firstname TEXT, 
    lastname TEXT, 
    PRIMARY KEY(username, email)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_info (
    username TEXT NOT NULL, 
    rounds INTEGER, 
    lose_rounds INTEGER, 
    win_rounds INTEGER, 
    points INTEGER, 
    lose_points INTEGER, 
    win_points INTEGER, 
    PRIMARY KEY(username), 
    FOREIGN KEY (username) REFERENCES signup_info (username)
);
""")

# Define variables
fullName = ""
firstName = ""
userName = ""
lastName = ""
userEmail = ""
password = ""
rePassword = ""

print("------------Sign up------------")
print("  Please enter your information  ")

def dataBase():
    cursor.execute("SELECT username, password, email FROM signup_info")
    alli = cursor.fetchall()
    userInfo = []
    for i in alli:
        userInfo.append(list(i))
    return userInfo

userInfo = dataBase()

def ValidPass():
    while True:
        password = input("Enter your password (must be at least 8 characters long and include at least one number) \n --> ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password):
            print("Password must include at least one number.")
        else:
            rePassword = input("Re-enter your password for confirmation \n --> ")
            if password == rePassword:
                return password
            else:
                print("Passwords do not match. Please try again.")

def signup():
    global fullName, firstName, lastName, userEmail, password, userName

    while True:
        fullName = input("Enter your full name \n --> ")
        if " " in fullName and fullName[0] != " ":
            firstName, lastName = fullName.split(" ", 1)
            break
        else:
            print("Please enter your full name with a space between first and last names.")

    while True:
        userName = input("Enter your username \n --> ")
        userName = forget(userName)
        if any(userName == user[0] for user in userInfo):
            print("This username is already taken.")
        else:
            break

    while True:
        userEmail = input("Enter your email address \n --> ")
        if "@" in userEmail:
            userEmail = forget(userEmail)
            if any(userEmail == user[2] for user in userInfo):
                print("This email address is already used.")
            else:
                break
        else:
            print("That's not a valid email address.")
            print("----------------------")

    password = ValidPass()

signup()

# Encrypt and hash user info
firstName = encrypt(firstName)
lastName = encrypt(lastName)
password = encrypt(password)

try:
    password = HashingInfo(password)
    print(f"Successfully signed up")
except Exception as e:
    print(f"An error occurred: {e}")

# Insert user info into the database
cursor.execute(f"INSERT INTO signup_info(username, password, email, firstname, lastname) VALUES(?, ?, ?, ?, ?)",
               (userName, password, userEmail, firstName, lastName))

# Save changes and close the database
db.commit()
db.close()
