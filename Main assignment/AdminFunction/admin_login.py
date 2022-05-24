from os.path import join, dirname
import json


def admin_login(username, password):
    path = join(dirname(__file__), "../Resources/admin_credentials.json")
    try:
        with open(path, "r") as file:
            data = json.load(file)
            user_name = data["user_name"]
            passwd = data["password"]
        if user_name == username and passwd == password:
            print("Login Successful")
            return True
        else:
            print("Invalid admin credentials")
            return False
    except FileNotFoundError as f:
        print(f)
        return False


if __name__ == "__main__":
    admin_login("admin", "adminpass")
