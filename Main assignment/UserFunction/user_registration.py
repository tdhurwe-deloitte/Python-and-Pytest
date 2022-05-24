import pandas as pd
from os.path import join, dirname
from csv import writer


def registration(cred_list):
    path = join(dirname(__file__), "../Resources/user_data.csv")
    data = pd.read_csv(path)
    username = data['Username'].tolist()
    email = data['Email'].tolist()
    # ls = [name, username, email, phone_no, age, password]
    if cred_list[1] not in username:
        if cred_list[2] not in email:
            try:
                with open(path, "a") as file:
                    writer_obj = writer(file)
                    writer_obj.writerow(cred_list)
                print("Registration Successful")
                return True
            except Exception as e:
                print("Registration Unsuccessful : ", e)
                return False
        else:
            print("Email is already in use")
            return False
    else:
        print("Username is already in use")
        return False


if __name__ == "__main__":
    cred_list = ["user1", "user1", "user1@gmail.com", 729012873, 42, "user1pass"]
    registration(cred_list)
