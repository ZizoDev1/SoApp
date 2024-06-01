# Import all required libraries and functions
from ncrpt import *
from hashing import *
import sqlite3

# Connect to the database file
db = sqlite3.connect("user_info.db")
cursor = db.cursor()

userName = ""
password = ""
email = ""

# Fetch user information from the database


def fetch_user_info():
    cursor.execute("SELECT username, password, email FROM signup_info")
    return cursor.fetchall()


userInfo = fetch_user_info()

# Count the number of users in the database


def count_users():
    return len(userInfo)


User_Counter = count_users()

# Function for user login


def login():
    global userName, password, email

    userName = input("Enter your username: ")
    password = input("Enter your password: ")

    encrypted_userName = encrypt(userName)
    encrypted_password = encrypt(password)

    try:
        # Hash the encrypted username and password
        hashed_userName = HashingInfo(encrypted_userName)
        hashed_password = HashingInfo(encrypted_password)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    error_counter = 0

    for user in userInfo:
        if hashed_userName == user[0] and hashed_password == user[1]:
            print("Login Successful")
            break
        else:
            error_counter += 1
            if error_counter == User_Counter:
                print("Username or Password is incorrect")


login()
