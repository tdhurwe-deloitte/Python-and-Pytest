from os.path import join, dirname
import pandas as pd


def user_login(username, password):
    path = join(dirname(__file__), "../Resources/user_data.csv")
    data = pd.read_csv(path)
    user_name = data['Username'].tolist()
    passwd = data['Password'].tolist()
    try:
        idx = user_name.index(username)
        if ((username in user_name) and (password in passwd)) and passwd[idx] == password:
            print("Login Successful")
            return True
        elif username not in user_name:
            print("Invalid username")
            return False
        elif passwd[idx] != password or password not in passwd:
            print("Wrong password")
            return False
        else:
            print("Invalid Credentials")
            return False
    except:
        print(f"{username} does not exist. ")
        return False


if __name__ == "__main__":
    user_login("user1", "user1pass")
