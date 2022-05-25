import pandas as pd
from os.path import join, dirname

def user_rating(movie_num, user):
    path = join(dirname(__file__), "../Resources/booking_data.csv")
    df = pd.read_csv(path)
    print("please enter rating for ", df.loc[movie_num, 'Movie name'])
    rating = int(input("Rating (out of 10) : "))
    r = str(rating)
    movie_list = df['Movie No.'].tolist()
    user_list = df['User name'].tolist()
    idx_movie = movie_list.index(movie_num)
    idx_user = user_list.index(user)
    if movie_list[idx_user] == movie_num:
        df.loc[idx_user, 'User rating'] = r
    elif user_list[idx_movie] == user:
        df.loc[idx_movie, 'User rating'] = r
    df.to_csv(path, index=False)
