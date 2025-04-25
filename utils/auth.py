import pandas as pd
import hashlib

USER_DATA_FILE = "data/user_data.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password, role):
    try:
        users = pd.read_csv(USER_DATA_FILE)
        user = users[(users["Username"] == username) & (users["Password"] == hash_password(password)) & (users["Role"] == role)]
        return not user.empty
    except FileNotFoundError:
        return False

def register_user(name, username, password, role, location):
    try:
        users = pd.read_csv(USER_DATA_FILE)
        if username in users["Username"].values:
            return False
        new_user = pd.DataFrame([[name, username, hash_password(password), role, location]], 
                                columns=["Name", "Username", "Password", "Role", "Location"])
        users = pd.concat([users, new_user], ignore_index=True)
    except FileNotFoundError:
        users = pd.DataFrame([[name, username, hash_password(password), role, location]], 
                             columns=["Name", "Username", "Password", "Role", "Location"])
    users.to_csv(USER_DATA_FILE, index=False)
    return True
