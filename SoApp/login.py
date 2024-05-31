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

username  = ""
password = ""
email = ""
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
User_Counter = 0
def count_login():
    global User_Counter
    for i in linfo :
        User_Counter += 1
    return User_Counter

User_Counter = count_login()
def login():
    global username,password,email

    user_name = input("Enter your username: ")
    pass_word = input("Enter your password: ")

    Username = encrypt(user_name)
    Password = encrypt(pass_word)
    try:
        # Call the hashing function and store the hashed password
        password = HashingInfo(Password)
        username = HashingInfo(Username)
    except Exception as e:
        print(f"An error occurred: {e}")

    checkererror = 0

    for i in linfo:
        if username == i[0] and password == i[1]:
            print("Login Successful")
            break
        else:
            checkererror += 1
            if checkererror == User_Counter :
                print("Username Or Password 's Incrorect")

login()