
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})


def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def update_user(user_id, name, email):
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            user["email"] = email


def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            break


add_user(3, "Charlie", "charlie@example.com")
print("After adding:", users)

print("Get user with ID 2:", get_user(2))

update_user(1, "Alicia", "alicia@example.com")
print("After updating:", users)

delete_user(2)
print("After deleting:", users)
