import sys
from AdminFunction import admin_login, add_movie, edit_movie_info, delete_movie
from UserFunction import user_login, user_registration, select_movie, movie_details, booking_tickets, cancling_tickets, user_rating

class Start:
    def start_page(self):
        while True:
            print(f"{'*'*20} Welcome to BookMyShow {'*'*20}")
            print("1. Login\n2. Register new account\n3. Exit")
            num = int(input("Enter : "))
            if num == 3:
                sys.exit(0)
            elif 0 < num <= 2:
                return num
            else:
                print("Please enter valid option \n")

    def login(self):
        while True:
            print(f"{'*' * 20} Welcome to BookMyShow {'*' * 20}")
            username = input("User : ")
            password = input("Password : ")
            if username == "admin":
                choice = admin_login.admin_login(username, password)
                if choice:
                    return "admin"
                else:
                    option = input("Try again (y/n) : ")
                    if option == "n" or option == "N":
                        break
            else:
                val = user_login.user_login(username, password)
                if val:
                    return username
                else:
                    option = input("Try again (y/n) : ")
                    if option == "n" or option == "N":
                        break
    def admin_dashboard(self):
        while True:
            print(f"{'*' * 20} Welcome Admin {'*' * 20}")
            print("1. Add New Movie Info \n2. Edit Movie Info \n3. Delete Movies\n4. Logout")
            choice = int(input("Enter : "))
            if 0 < choice < 5:
                return choice
            else:
                print("Please Enter valid option")


class Registration:
    def user_registration(self):
        while True:
            print(f"{'*' * 20} Create New Account {'*' * 20}")
            # ls = [name, username, email, phone_no, age, password]
            name = input("Name : ")
            username = input("Username : ")
            email = input("Email : ")
            phone_no = input("Phone no. : ")
            age = input("Age : ")
            password = input("Password : ")
            ls = [name, username, email, phone_no, age, password]
            val = user_registration.registration(ls)
            if val:
                break
            else:
                option = input("Try again (y/n) : ")
                if option == "n" or option == "N":
                    break


if __name__ == "__main__":
    while True:
        start = Start()
        option = start.start_page()
        if option == 1:
            val = start.login()
            if val == "admin":
                while True:
                    opt = start.admin_dashboard()
                    if opt == 1:
                        add_movie.add_movie_dashboard()
                    elif opt == 2:
                        edit_movie_info.edit_movie()
                    elif opt == 3:
                        delete_movie.delete_movie()
                    elif opt == 4:
                        break
            else:
                while True:
                    choice, total = select_movie.select_movie()
                    if choice == total:
                        break
                    opt = movie_details.movie_details(choice)
                    if opt == 1:
                        booking_tickets.book_tickets(choice, val)
                    elif opt == 2:
                        cancling_tickets.cancel_tickets(choice, val)
                    elif opt == 3:
                        user_rating.user_rating(choice, val)
        elif option == 2:
            register = Registration()
            register.user_registration()





