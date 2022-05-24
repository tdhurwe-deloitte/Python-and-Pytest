import pandas as pd
from os.path import join, dirname
from csv import writer


def book_tickets(movie_num, user):
    path = join(dirname(__file__), "../Resources/movie_data.csv")
    path2 = join(dirname(__file__), "../Resources/booking_data.csv")
    df = pd.read_csv(path)
    # function to get timings
    slots = df['Timings'].tolist()
    t = slots[movie_num]
    s = t.split(" | ")
    for i in range(len(s)):
        print(f"{i}. {s[i]}")
    slot = int(input("Select slot : "))
    # timings = int(input("Select Timings : "))
    seats = int(df.iloc[movie_num]['Capacity'])
    print("Remaining seats : ", seats)
    movie_name = df.iloc[movie_num]['Title']
    while True:
        num_of_seats = int(input("Enter number of seats : "))
        if num_of_seats <= seats:
            ls = [user, movie_num + 1, movie_name, num_of_seats, s[slot]]
            with open(path2, 'a') as file:
                writer_obj = writer(file)
                writer_obj.writerow(ls)
                file.close()
            remaining_seat = seats - num_of_seats
            df.loc[movie_num, 'Capacity'] = remaining_seat
            df.to_csv(path, index=False)
            print("Tickets booked successfully ")
            break
        else:
            print("Please Enter valid number of seats")


if __name__ == "__main__":
    book_tickets()
