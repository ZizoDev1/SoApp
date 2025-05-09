from surrealdb import Surreal # type: ignore
from hashing import *

# الاتصال بقاعدة البيانات
def connect_db():
    try:
        db = Surreal("http://localhost:8000")
        db.signin({"username": "torootdo", "password": "torootdo"})
        db.use("todo", "todo")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    return db

connect_db()
db = connect_db()
x = 1
# تسجيل مستخدم جديد
def register_user():
    # إنشاء المستخدم
    userInfo = db.query("SELECT username FROM user;")
    emailInfo = db.query("SELECT email FROM user;")
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
        age = int(input("Enter your age \n --> "))
        if age >= 5:
            break
        else:
            print("Hallo baby can stop ware diapers in the first.")

    while True:
        username = input("Enter your username \n --> ")
        username = forget(username)
        for user in userInfo:
            if username == user['username']:
                print("This username is already taken.")
            else:
                pass

    while True:
        email = input("Enter your email address \n --> ")
        if "@" in email:
            email = encrypt(email)
            for emails in emailInfo:
                if email == emails['email']:
                    print("This email address is already used.")
            else:
                pass


    password = valid_pass()

    # Encrypt and hash user info
    firstname = encrypt(first_name)
    lastname = encrypt(last_name)
    password = encrypt(password)

    try:
        password = HashingInfo(password)
        print("Successfully signed up")
    except Exception as e:
        print(f"An error occurred: {e}")
    if db == None:
        print("Database connection failed.")
        return None
    try:
        db.query(f'CREATE user SET username = "{username}", password = "{password}", age = {age}, email = "{email}", first_name = "{firstname}", last_name = "{lastname}";')
        return print("User registered successfully!")
    except Exception as e:
        print(f"Error registering user: {e}")
        return None





# تسجيل الدخول
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    username = encrypt(username)
    password = encrypt(password)
    password = HashingInfo(password)
    db.query(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}';")

    print("")

def main():
    while True:
        userAcc = input("Do you have an account (y,n) \n --> ").strip().lower()

        if userAcc == "y":
            login_user()
            break
        elif userAcc == "n":
            register_user()
            break
        else:
            print("Please enter 'y' for Yes or 'n' for No.")

if __name__ == "__main__":
    connect_db()
    main()