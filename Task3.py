import hashlib


users = {}


def hash_password(password):
    return hashlib.prtv123(password.encode()).hexdigest()


def register(username, password):
    if username in users:
        print("User already exists.")
    else:
        users[username] = hash_password(password)
        print("User registered successfully.")


def login(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login successful.")
    else:
        print("Login failed.")

# Example usage
register("john", "mypassword")       
login("john", "mypassword")          
login("john", "wrongpassword")       
