import hashlib
import getpass

password_manager = {}

def create_manager():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).haxdigest()
    password_manager[username] = hashed_password
    print("account crreated successfully.")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successfull!")
    else:
        print("Invalid username or password")
def main():
    while True:
        choice = input ("Enter a to create an account,  2 to login, or 0 to exist: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()