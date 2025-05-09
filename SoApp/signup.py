# Import all required libraries and functions
from ncrpt import *
from hashing import *
# import sqlite3
from SurrealDB import main, connect_db
# db = sqlite3.connect("user_info.db")
# cursor = db.cursor()


def fetch_user_info():
    db = connect_db()
    return db.query("SELECT username, password, email FROM signup_info")



def fetch_signup_info():
    db = connect_db()
    return db.query("SELECT username, password, email, firstname, lastname FROM signup_info")

userInfo = fetch_user_info()
userall = fetch_signup_info()


def signup():
    def valid_pass():
        while True:
            password = input(
                "Enter your password (must be at least 8 characters long and include at least one number) \n --> ")
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
            elif not any(char.isdigit() for char in password):
                print("Password must include at least one number.")
            else:
                re_password = input("Re-enter your password for confirmation \n --> ")
                if password == re_password:
                    return password
                else:
                    print("Passwords do not match. Please try again.")

    while True:
        full_name = input("Enter your full name \n --> ")
        if " " in full_name and full_name[0] != " ":
            first_name, last_name = full_name.split(" ", 1)
            break
        else:
            print("Please enter your full name with a space between first and last names.")
    
    while True:
        age = input("Enter your age \n --> ")
        if int(age) >= 5:
            break
        else:
            print("Hallo baby can stop ware diapers in the first.")

    while True:
        user_name = input("Enter your username \n --> ")
        user_name = forget(user_name)
        if any(user_name == user[0] for user in userInfo):
            print("This username is already taken.")
        else:
            break

    while True:
        user_email = input("Enter your email address \n --> ")
        if "@" in user_email:
            user_email = encrypt(user_email)
            if any(user_email == user[1] for user in userInfo):
                print("This email address is already used.")
            else:
                break
        else:
            print("That's not a valid email address.")
            print("----------------------")

    password = valid_pass()

    # Encrypt and hash user info
    first_name = encrypt(first_name)
    last_name = encrypt(last_name)
    password = encrypt(password)

    try:
        password = HashingInfo(password)
        print("Successfully signed up")
    except Exception as e:
        print(f"An error occurred: {e}")

    main(1, user_name, password, age, user_email, first_name, last_name)
