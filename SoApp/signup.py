# Import all required libraries and functions
from ncrpt import *
from hashing import *
import sqlite3

db = sqlite3.connect("user_info.db")
cursor = db.cursor()


def fetch_user_info(cursor):
    cursor.execute("SELECT username, email FROM signup_info")
    return cursor.fetchall()


def fetch_signup_info(cursor):
    cursor.execute("SELECT username, password, email, firstname, lastname FROM signup_info")
    return cursor.fetchall()


userInfo = fetch_user_info(cursor)
userall = fetch_signup_info(cursor)

def signup():
    global cursor

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
        user_name = input("Enter your username \n --> ")
        user_name = forget(user_name)
        if any(user_name == user[0] for user in userInfo):
            print("This username is already taken.")
        else:
            break

    while True:
        user_email = input("Enter your email address \n --> ")
        if "@" in user_email:
            user_email = forget(user_email)
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

    try:
        cursor.execute("INSERT INTO signup_info(username, password, email, firstname, lastname) VALUES(?, ?, ?, ?, ?)",
                       (user_name, password, user_email, first_name, last_name))
        db.commit()
    except sqlite3.IntegrityError:
        print("An error occurred while signing up: This email is already registered.")

    db.close()
