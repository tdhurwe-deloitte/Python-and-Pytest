import pandas as pd

# creating csv file for users

user_col_name = ["Name", "Username", "Email", "Phone No.", "Age", "Password"]
user_df = pd.DataFrame(columns=user_col_name)
user_df.to_csv("user_data.csv", index=False)

# creating csv file for movie data
movie_col_name = ["Title", "Genre", "Length", "Cast", "Director", "Admin rating", "Language", "Timings", "No. of shows", "First show", "Interval time", "Gap b/w shows", "Capacity"]
movie_df = pd.DataFrame(columns=movie_col_name)
movie_df.to_csv("movie_data.csv", index=False)

# creating csv file for booking data
booking_col_name = ["User name", "Movie No.", "Movie Name", "Seats", "Timing", "User rating"]
booking_df = pd.DataFrame(columns=booking_col_name)
booking_df.to_csv("booking_data.csv", index=False)
