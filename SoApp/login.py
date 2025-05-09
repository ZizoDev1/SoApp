# Import all required libraries and functions
from ncrpt import *
from hashing import *
from SurrealDB import main, connect_db

userName = ""
password = ""
email = ""

# Fetch user information from the database


def fetch_user_info():
    db = connect_db()
    return db.query("SELECT username, password FROM signup_info")



userInfo = fetch_user_info()

# Count the number of users in the database


def count_users():
    return len(userInfo)


User_Counter = count_users()

# Function for user login


def login():
    global userName, password

    userName = input("Enter your username: ")
    password = input("Enter your password: ")

    encrypted_userName = encrypt(userName)
    encrypted_password = encrypt(password)

    try:
        # Hash the encrypted password
        hashed_password = HashingInfo(encrypted_password)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    main(2, encrypted_userName, hashed_password, 5, "dd@gg.gg", "ff", "ll")