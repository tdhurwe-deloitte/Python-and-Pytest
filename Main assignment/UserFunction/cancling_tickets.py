from os.path import join, dirname
import pandas as pd


def cancel_tickets(movie_num, user):
    path = join(dirname(__file__), "../Resources/movie_data.csv")
    path2 = join(dirname(__file__), "../Resources/booking_data.csv")
    df = pd.read_csv(path)
    seats = int(df.iloc[movie_num]['Capacity'])
    df2 = pd.read_csv(path2)
    ls = df2['User name'].tolist()
    pos = ls.index(user)
    seats_booked = int(df2.iloc[pos]['Seats'])
    while True:
        num = int(input("Number of seats you want to cancel : "))
        if num <= seats_booked:
            seats = seats + num
            seats_booked = seats_booked - num
            df.loc[movie_num, 'Capacity'] = seats
            df2.loc[pos, 'Seats'] = seats_booked
            print("Ticket canceled successfully")
            break
        else:
            print("Please enter valid number of seats")
