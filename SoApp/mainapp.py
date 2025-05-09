from signup import signup
from login import login


def main():
    while True:
        userAcc = input("Do you have an account (y,n) \n --> ").strip().lower()

        if userAcc == "y":
            login()
            break
        elif userAcc == "n":
            signup()
            break
        else:
            print("Please enter 'y' for Yes or 'n' for No.")

if __name__ == "__main__":
    main()
