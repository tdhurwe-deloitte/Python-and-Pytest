import pandas as pd
from os.path import join, dirname

def delete_movie():
    path = join(dirname(__file__), "../Resources/movie_data.csv")
    data = pd.read_csv(path)
    for i in range(data.shape[0]):
        print(f"{i + 1} . {data.iloc[i][0]}")

    choice = int(input("Enter : "))
    choice -= 1
    try:
        data.drop(choice, inplace=True)
        print("Movie Deleted Successfully")
    except Exception as e:
        print(f"Task Failed : {e}")


if __name__ == "__main__":
    delete_movie()
