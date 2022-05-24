import pandas as pd
from os.path import join, dirname


def movie_details(movie_num):
    ls = [
        "Title : ",
        "Genre : ",
        "Length(in min) : ",
        "Cast : ",
        "Director : ",
        "Admin rating : ",
        "Language : ",
        "Timings : ",
        "Number of shows in a day : ",
        "First show : ",
        "Interval time : ",
        "Gap between shows : ",
        "Capacity : "
    ]
    path = join(dirname(__file__), "../Resources/movie_data.csv")
    df = pd.read_csv(path)
    for i in range(df.shape[1]):
        print(ls[i], df.iloc[movie_num][i])

    print("1. Book Tickets\n2. Cancel Tickets\n3. Give User Rating")
    choice = int(input("Enter : "))
    return choice


if __name__ == "__main__":
    movie_details(5)
