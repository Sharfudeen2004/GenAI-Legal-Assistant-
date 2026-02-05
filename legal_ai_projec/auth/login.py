import json
import os

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")

def authenticate(username, password):
    try:
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
        # Debug print (can remove in production)
        print("Users in file:", users)
        print("Trying login:", username, password)
        return users.get(username) == password
    except Exception as e:
        print(f"Login error: {e}")
        return False