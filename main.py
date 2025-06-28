import hashlib
import getpass

password_manager = {}

def create_manager():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).haxdigest()
    password_manager[username] = hashed_password
    print("account crreated successfully.")