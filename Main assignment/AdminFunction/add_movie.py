from csv import writer
from os.path import join, dirname
from datetime import datetime, timedelta


def add_movie_dashboard():
    ls = ["Title : ",
          "Genre : ",
          "Length(in min) : ",
          "Cast : ",
          "Director : ",
          "Admin rating : ",
          "Language : ",
          "Number of shows in a day : ",
          "First show(hh:MM) : ",
          "Interval time (in minutes) : ",
          "Gap between shows : ",
          "Capacity : "
          ]

    ls2 = []
    for i in range(len(ls)):
        value = input(f"{ls[i]}")
        ls2.append(value)
    movie_length = ls2[2]
    hr = int(movie_length) // 60
    minute = int(movie_length) % 60
    tot = "{} hr: {} min".format(hr, minute)
    ls2[2] = tot
    timings = calculate_interval(int(movie_length), ls2[8], int(ls2[9]), int(ls2[10]), int(ls2[7]))
    ls2.insert(7, timings)
    path = join(dirname(__file__), "../Resources/movie_data.csv")
    try:
        with open(path, "a") as file:
            writer_obj = writer(file)
            writer_obj.writerow(ls2)
        print("Movie added successfully")
    except Exception as e:
        print(f"Failed to add new data : {e}")


def calculate_interval(movie_length, first_show, interval, gap, number_of_shows):
    movie_length_with_interval = int(movie_length) + int(interval)
    hr = movie_length_with_interval // 60
    minutes = movie_length_with_interval % 60
    timings = []
    for i in range(number_of_shows):
        time_format = "%H:%M"
        date_time_obj = datetime.strptime(first_show, time_format)
        end_time = date_time_obj + timedelta(hours=hr, minutes=minutes)
        s = f"{end_time.hour}:{end_time.minute}"
        string = f"{first_show} - {s}"
        timings.append(string)
        new_start_time = datetime.strptime(s, time_format)
        k = new_start_time + timedelta(minutes=gap)
        first_show = f"{k.hour}:{k.minute}"

    all_timings = " | ".join(timings)
    return all_timings


if __name__ == "__main__":
    add_movie_dashboard()
